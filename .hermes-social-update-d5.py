#!/usr/bin/env python3
import json
import sqlite3
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
REQUEST_KEY = 'social-d5d16909b0f33f9a0bc007d9'
UPDATED_AT = '2026-10-08T09:19:52-03:00'
COPY_TEXT = '''CAPA
Se uma pessoa assume e o cliente precisa contar tudo de novo,

o atendimento não foi transferido.

Foi reiniciado.

LEGENDA
A automação resolve até o pedido sair do roteiro.

Quando isso acontece, alguém precisa entrar sem perder a conversa, as decisões e o que já foi tentado.

Uma atualização da Zendesk deixou esse ponto mais visível: agora, pessoas autorizadas podem assumir conversas conduzidas por agente de IA. Quando isso acontece, a IA para, a pessoa vira responsável e a troca fica registrada no histórico.

A novidade é da Zendesk. O princípio vira uma pergunta útil para qualquer atendimento automatizado:

— Quem pode assumir?
— O que essa pessoa recebe?
— A automação realmente para?
— A troca fica registrada?

É esse tipo de passagem que a Simplifique ajuda a organizar antes de escolher ou conectar a ferramenta: regra clara, contexto preservado e responsabilidade definida.

CTA
Escolha um atendimento automatizado e confira: quando uma pessoa assume, ela recebe a conversa inteira?'''

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
try:
    con.execute('BEGIN IMMEDIATE')
    row = con.execute(
        'select request_key,status,copy_text,decision from social_content_requests where request_key=?',
        (REQUEST_KEY,),
    ).fetchone()
    if row is None:
        raise RuntimeError('request_key not found')
    if row['status'] not in ('queued', 'copy_in_production'):
        raise RuntimeError(f"unexpected status: {row['status']}")
    con.execute(
        '''update social_content_requests
           set status='copy_review', copy_text=?, decision=NULL,
               approved_by=NULL, approved_at=NULL, figma_url=NULL, updated_at=?
           where request_key=?''',
        (COPY_TEXT, UPDATED_AT, REQUEST_KEY),
    )
    con.commit()
    readback = dict(con.execute(
        '''select request_key,topic_key,topic_title,desired_format,copy_text,planned_for,
                  decision,decision_note,approved_by,approved_at,figma_url,status,
                  requester,requested_at,updated_at
           from social_content_requests where request_key=?''',
        (REQUEST_KEY,),
    ).fetchone())
    print(json.dumps(readback, ensure_ascii=False, indent=2))
finally:
    con.close()
