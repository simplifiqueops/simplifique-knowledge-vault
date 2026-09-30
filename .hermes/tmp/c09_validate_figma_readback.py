import json
from pathlib import Path

path = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08/L08-C09-contexto-agente/qa-screenshots/figma-readback-image-revision.json')
data = json.loads(path.read_text(encoding='utf-8'))
frame_ids = ['328:69','328:70','328:71','328:72','328:73','328:74']

def find_node(obj, node_id):
    if isinstance(obj, dict):
        if obj.get('id') == node_id:
            return obj
        for value in obj.values():
            found = find_node(value, node_id)
            if found:
                return found
    elif isinstance(obj, list):
        for value in obj:
            found = find_node(value, node_id)
            if found:
                return found
    return None

def visible_descendants(node):
    for child in node.get('children', []):
        if child.get('visible', True):
            yield child
            yield from visible_descendants(child)

report = []
for frame_id in frame_ids:
    frame = find_node(data, frame_id)
    box = frame.get('absoluteBoundingBox')
    issues = []
    if not box or round(box['width']) != 1080 or round(box['height']) != 1350:
        issues.append('frame_dimensions')
    if box:
        left, top = box['x'], box['y']
        right, bottom = left + box['width'], top + box['height']
        for child in visible_descendants(frame):
            child_box = child.get('absoluteBoundingBox')
            if not child_box:
                continue
            c_left, c_top = child_box['x'], child_box['y']
            c_right, c_bottom = c_left + child_box['width'], c_top + child_box['height']
            if c_left < left - 0.5 or c_top < top - 0.5 or c_right > right + 0.5 or c_bottom > bottom + 0.5:
                issues.append({'outside': child.get('id'), 'name': child.get('name'), 'box': child_box})
    report.append({'id': frame_id, 'name': frame.get('name'), 'width': box.get('width') if box else None, 'height': box.get('height') if box else None, 'clipsContent': frame.get('clipsContent'), 'issues': issues})
image = find_node(data, '337:74')
overlay = find_node(data, '337:75')
print(json.dumps({'frames': report, 'image': {'id': image.get('id'), 'name': image.get('name'), 'fill': image.get('fills'), 'box': image.get('absoluteBoundingBox')}, 'overlay': {'id': overlay.get('id'), 'name': overlay.get('name'), 'box': overlay.get('absoluteBoundingBox')}}, ensure_ascii=False, indent=2))
