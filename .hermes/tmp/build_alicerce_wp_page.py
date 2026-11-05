#!/usr/bin/env python3
import html
import json
from pathlib import Path

ASSETS = json.loads(Path('/home/simplifique/vault/.hermes/tmp/alicerce-wp-assets.json').read_text(encoding='utf-8'))
U = {k:v['url'] for k,v in ASSETS.items()}
ASSET_DIR = Path('/home/simplifique/vault/01-Clientes/Realizando-Potenciais/Alicerce-do-Extraordinario/Pagina-de-Vendas/assets/editorial')
EXEC_DIR = Path('/tmp/alicerce-figma-exec')
OUT_DIR = Path('/home/simplifique/vault/01-Clientes/Realizando-Potenciais/Alicerce-do-Extraordinario/Pagina-de-Vendas/wordpress')
OUT_DIR.mkdir(parents=True, exist_ok=True)


def e(s): return html.escape(s, quote=True)
def paras(text): return ''.join(f'<p>{e(p)}</p>' for p in text.split('\n\n') if p)
def lines(text, cls=''): return ''.join(f'<li class="{cls}">{e(x.lstrip("•✓ "))}</li>' for x in text.splitlines() if x.strip())
def cta(label, secondary=False):
    cls='cta secondary' if secondary else 'cta'
    return f'<button type="button" class="{cls}" aria-disabled="true" title="Destino ainda não definido">{e(label)}</button>'
def actions(primary, team=True):
    return '<div class="actions">'+cta(primary)+(cta('FALE COM A EQUIPE HUMANA',True) if team else '')+'</div>'
def img(key, alt): return f'<img src="{e(U[key])}" alt="{e(alt)}" loading="lazy">'
def card(kicker,title,body,key=None,extra=''):
    media=f'<div class="card-media">{img(key,title)}</div>' if key else ''
    return f'<article class="card {extra}">{media}<div class="card-body"><span class="eyebrow">{e(kicker)}</span><h3>{e(title)}</h3><p>{e(body)}</p></div></article>'

def testimonial(name,role,headline,body,quote,cta_label):
    return f'''<article class="story">
      <div class="story-media"><span class="play">▶</span><strong>ASSISTA À HISTÓRIA<br>DE {e(name.upper())}</strong><small>INSERIR VÍDEO ORIGINAL</small></div>
      <div class="story-copy"><span class="tag">HISTÓRIA REAL · {e(role)}</span><h3>{e(headline)}</h3>{paras(body)}<blockquote>{e(quote)}</blockquote>{actions(cta_label)}</div>
    </article>'''

css=r'''
@import url('https://fonts.googleapis.com/css2?family=Lora:wght@600&family=Manrope:wght@400;600;700&display=swap');
:root{--ink:#242827;--dark:#0e2325;--deep:#082225;--green:#2b5150;--cream:#f7f1e3;--paper:#fbf8f0;--gold:#f1dec0;--brick:#8c4b44;--yellow:#ffd10d;--white:#fff;--shadow:0 18px 48px rgba(8,34,37,.13)}
*{box-sizing:border-box}.alicerce-page{margin:0;background:var(--paper);color:var(--ink);font-family:Manrope,Arial,sans-serif;font-size:17px;line-height:1.55;overflow:hidden}.alicerce-page h1,.alicerce-page h2,.alicerce-page h3{font-family:Lora,Georgia,serif;font-weight:600;line-height:1.15;margin:0}.alicerce-page p{margin:0 0 1em}.alicerce-page img{display:block;width:100%;height:100%;object-fit:cover}.alicerce-page .section{position:relative;padding:88px 24px;border-bottom:2px solid rgba(43,81,80,.22)}.alicerce-page .dark{background:var(--dark);color:var(--cream)}.alicerce-page .cream{background:var(--cream)}.alicerce-page .paper{background:var(--paper)}.alicerce-page .wrap{width:min(1232px,100%);margin:0 auto}.alicerce-page .narrow{width:min(1120px,100%);margin:0 auto}.alicerce-page .kicker,.alicerce-page .eyebrow,.alicerce-page .tag{display:block;font-weight:700;letter-spacing:.12em;text-transform:uppercase;font-size:.78rem;margin-bottom:18px}.alicerce-page .dark .kicker,.alicerce-page .dark .eyebrow{color:var(--gold)}.alicerce-page .section-title{font-size:clamp(2.1rem,4.4vw,4.2rem);max-width:1080px;margin-bottom:24px}.alicerce-page .section-sub{font-size:1.15rem;max-width:1000px;margin-bottom:38px}.alicerce-page .grid{display:grid;gap:28px}.alicerce-page .grid-2{grid-template-columns:repeat(2,minmax(0,1fr))}.alicerce-page .grid-3{grid-template-columns:repeat(3,minmax(0,1fr))}.alicerce-page .grid-4{grid-template-columns:repeat(4,minmax(0,1fr))}.alicerce-page .card{border:1px solid rgba(43,81,80,.22);border-radius:18px;background:rgba(255,255,255,.66);overflow:hidden;box-shadow:0 8px 24px rgba(8,34,37,.05);display:flex;flex-direction:column;min-width:0}.alicerce-page .dark .card{background:#193c3f;border-color:rgba(241,222,192,.55);box-shadow:none}.alicerce-page .card-media{height:108px}.alicerce-page .card-body{padding:26px}.alicerce-page .card h3{font-family:Manrope,Arial,sans-serif;font-size:1.25rem;margin-bottom:12px}.alicerce-page .card p{margin:0}.alicerce-page .actions{display:flex;justify-content:center;align-items:center;gap:18px;flex-wrap:wrap;margin-top:44px}.alicerce-page .cta{appearance:none;border:0;border-radius:999px;background:var(--gold);color:var(--deep);font:700 .85rem/1 Manrope,Arial,sans-serif;letter-spacing:.06em;padding:21px 34px;min-width:310px;cursor:default}.alicerce-page .cta.secondary{background:transparent;color:var(--gold);border:1.5px solid var(--gold)}.alicerce-page .paper .cta.secondary,.alicerce-page .cream .cta.secondary{color:var(--deep);border-color:var(--deep)}
.hero{min-height:720px;display:flex;align-items:center;background:radial-gradient(circle at 82% 27%,rgba(241,222,192,.18),transparent 28%),linear-gradient(135deg,#082225,#14383a 65%,#0e2325);color:var(--cream)}.hero .wrap{display:grid;grid-template-columns:minmax(0,760px) 1fr;gap:80px;align-items:center}.hero h1{font-size:clamp(2.7rem,5vw,4.8rem);margin:18px 0 26px}.hero .promise-list{list-style:none;padding:0;margin:0 0 28px;display:grid;gap:8px}.hero .promise-list li:before{content:'•';color:var(--gold);margin-right:10px}.hero .hero-mark{aspect-ratio:1;border-radius:50%;border:1px solid rgba(241,222,192,.28);position:relative}.hero .hero-mark:before,.hero .hero-mark:after{content:'';position:absolute;border:1px solid rgba(241,222,192,.22);border-radius:50%;inset:12%}.hero .hero-mark:after{inset:30%;background:radial-gradient(circle,rgba(241,222,192,.2),transparent 65%)}
.video-box{height:430px;border-radius:24px;background:linear-gradient(145deg,#173b3d,#071b1e);border:1px solid rgba(241,222,192,.35);display:grid;place-items:center;text-align:center;margin:40px 0}.video-box .play,.story-media .play{display:block;font-size:4rem;color:var(--gold);margin-bottom:14px}.learning{columns:2;column-gap:50px;list-style:none;padding:0}.learning li{break-inside:avoid;margin:0 0 18px;padding-left:24px;position:relative}.learning li:before{content:'•';position:absolute;left:0;color:var(--gold)}
.friction .card-media{height:165px}.friction-transition{font-family:Lora,Georgia,serif;font-size:clamp(1.5rem,2.6vw,2.25rem);margin-top:44px;max-width:1100px}.friction-transition strong{color:var(--brick)}
.qual-list{list-style:none;padding:0;margin:24px 0;display:grid;grid-template-columns:1fr 1fr;gap:13px 38px}.qual-list li{padding-left:28px;position:relative}.qual-list li:before{content:'✓';position:absolute;left:0;color:var(--green);font-weight:700}.areas{font-weight:700;letter-spacing:.07em;text-transform:uppercase;margin:28px 0}.ethical{border-left:4px solid var(--green);padding:18px 24px;background:rgba(255,255,255,.42)}
.journey .card{min-height:215px}.stage .card-media{height:92px}.stage .note{margin-top:24px;font-size:.9rem;opacity:.78}.summary{font-family:Lora,Georgia,serif;font-size:clamp(1.5rem,2.5vw,2.1rem);text-align:center;margin:44px auto 0;max-width:900px}
.stories .section-title{text-align:center;margin-inline:auto}.story{display:grid;grid-template-columns:42% 58%;margin:34px 0;border-radius:22px;overflow:hidden;background:#fff;box-shadow:var(--shadow)}.story-media{min-height:520px;background:linear-gradient(150deg,#173f41,#071b1e);display:grid;align-content:center;justify-items:center;text-align:center;color:var(--gold);padding:36px}.story-media small{margin-top:10px;opacity:.75}.story-copy{padding:48px}.story-copy h3{font-size:clamp(1.7rem,2.6vw,2.5rem);margin-bottom:26px}.story-copy blockquote{margin:28px 0;padding:22px;border-left:4px solid var(--green);background:var(--cream);font-weight:600;white-space:pre-line}.story-copy .actions{justify-content:flex-start;margin-top:28px}.story-copy .cta{min-width:250px}
.execution .card-media{height:120px}.quote{font-family:Lora,Georgia,serif;font-size:1.6rem;text-align:center;margin:44px auto 0;max-width:900px}.guarantee{padding:36px;background:#fff;border:2px solid var(--green);border-radius:18px}.guarantee h3{font-family:Manrope,Arial,sans-serif;margin-bottom:14px}.creators .creator{background:#fff;border-radius:22px;overflow:hidden;box-shadow:var(--shadow)}.creator-photo{height:420px}.creator-body{padding:34px}.creator-body h3{font-size:1.6rem;margin-bottom:22px}.creator-body p{white-space:normal}.reasons .reason{display:grid;grid-template-columns:70px 1fr;gap:22px;padding:24px 0;border-bottom:1px solid rgba(43,81,80,.25)}.reason .num{font:600 1.5rem Lora,serif;color:var(--green)}.reason h3{font-family:Manrope,Arial,sans-serif;font-size:1.25rem;margin-bottom:8px}
.offer{background:var(--deep);color:var(--cream)}.offer .kicker{font-size:1.35rem;color:var(--yellow)}.offer-table{border:3px solid var(--brick);border-radius:22px;background:var(--cream);color:var(--ink);padding:34px;box-shadow:0 22px 60px rgba(0,0,0,.3)}.offer-table h3{font-family:Manrope,Arial,sans-serif;font-size:1.35rem;margin-bottom:18px}.offer-list{list-style:none;padding:0;margin:0}.offer-list li{padding:10px 0;border-bottom:1px solid rgba(43,81,80,.15)}.anchor{text-align:center;margin:34px 0 22px;font-weight:700}.anchor .old{display:block;color:var(--brick);font:600 3.2rem Lora,serif;text-decoration:line-through;text-decoration-thickness:4px}.price-box{border:3px solid var(--yellow);border-radius:20px;padding:34px;text-align:center;box-shadow:0 18px 50px rgba(140,75,68,.35)}.deadline{display:inline-block;background:var(--brick);color:#fff5c7;border-radius:999px;padding:9px 20px;font-weight:700}.discount{font-size:1.3rem;margin:18px 0 4px}.price{font:600 clamp(2.8rem,5vw,4.4rem)/1 Lora,serif}.cash{color:var(--gold);font-size:1.2rem;margin-top:10px}.footer{background:#071b1e;color:var(--cream);text-align:center;font-size:.82rem}.footer .legal{margin:12px 0}.footer .disclaimer{max-width:1100px;margin:auto;opacity:.78}
@media(max-width:900px){.alicerce-page{font-size:16px}.alicerce-page .section{padding:64px 24px}.grid-4,.grid-3,.grid-2{grid-template-columns:1fr}.hero{min-height:auto}.hero .wrap{grid-template-columns:1fr;gap:34px}.hero .hero-mark{display:none}.hero h1{font-size:2.65rem}.learning{columns:1}.qual-list{grid-template-columns:1fr}.story{grid-template-columns:1fr}.story-media{min-height:330px}.creator-photo{height:360px}.card-media{height:150px}.stage .card-media{height:115px}}
@media(max-width:520px){.alicerce-page .section{padding:52px 24px}.alicerce-page .section-title{font-size:2.05rem}.hero h1{font-size:2.25rem}.video-box{height:300px}.actions{display:grid}.cta{min-width:0;width:100%;padding:18px 22px}.story-copy{padding:30px 24px}.story-copy .actions{justify-content:stretch}.story-copy .cta{min-width:0}.offer-table,.price-box{padding:24px 20px}.anchor .old{font-size:2.35rem}.price{font-size:2.5rem}.creator-photo{height:310px}}
'''

stories = [
('Paloma','PERSONAL TRAINER','Ela tinha pós-graduação e experiência internacional. E chegou a vender saquinhos de lixo no semáforo.',
'''Uma história sobre conhecimento, dificuldades emocionais e a reconstrução de uma trajetória profissional.

Paloma se mudou para São Paulo para desenvolver seu negócio. Tinha formação extensa, experiência e conhecimento. Mas, após um período emocionalmente difícil, ficou sem trabalho e sem condições de manter o apartamento.

Passou a comer em um restaurante comunitário de R$1, procurou diferentes trabalhos e chegou a vender saquinhos de lixo no semáforo para conseguir dinheiro.

A reconstrução da Paloma começou com a fase de DESTRAVAR, com foco em desativar os padrões automáticos de sobrevivência que a faziam paralisar diante dos desafios emocionais.

Logo depois desse processo ela voltou a trabalhar em sua área, recebeu propostas salariais muito superiores e, com o tempo, conseguiu quitar mais de R$ 45 mil em dívidas bancárias.

O conhecimento técnico como personal trainer ela já tinha. O que precisou reconstruir foram as condições emocionais para colocá-lo em movimento.

Em outros relatos, Paloma também conta que passou a gravar vídeos, se posicionar profissionalmente e participou de um programa de TV.''',
'“Cara, o que eu tô fazendo aqui? Eu tenho tanto conhecimento, eu sei tanta coisa. Eu sou boa no que eu faço. Mas eu precisava do dinheiro.”\n\n“No dia que eu paguei eu chorei.”','QUERO ME RECONSTRUIR'),
('Gicela','PSICÓLOGA','Ela já tinha vinte anos de experiência. O próximo passo foi levar seu conhecimento a novos formatos.',
'''Da experiência profissional à construção de grupos e experiências de aprendizagem.

Gicela é psicóloga e atua com o público cristão. Sua formação e experiência já existiam antes de começar a explorar novos formatos.

Após um atendimento de Botão de Emergência com orientações sobre o pilar de CONSTRUIR (posicionamento nas redes sociais e foco em tirar projetos da gaveta) desenvolveu conteúdos e novos formatos de entrega.

Criou imersões online, presenciais e até mesmo um produto digital. E já está se organizando para expandir sua comunidade para formação de profissionais.''',
'“Eu já sabia tudo isso, mas você organizou de um jeito que fez toda diferença.”\nGicela Alves','QUERO ESCALAR'),
('Andrea','MENTORA E ALFABETIZADORA CORPORAL','Quatro curtidas em um post. Uma venda de R$ 6 mil.',
'''Uma experiência que mostra por que popularidade e valor comercial não são a mesma coisa.

Andrea já possuía experiência em seu trabalho como Alfabetizadora Corporal e Mentora e já tinha vivido uma cura espontânea de 6 anos de fibromialgia após um atendimento em grupo no contexto de SUSTENTAR.

Após aplicar orientações de comunicação e posicionamento das redes sociais que serão ensinadas na Imersão Presença Digital, relatou mais leveza e consistência para criar conteúdos.

Em um de seus relatos, contou que uma publicação com apenas quatro curtidas esteve ligada à venda de um produto de R$ 6 mil.

Não é o número de curtidas que, isoladamente, define se uma comunicação chegou à pessoa certa. É a presença digital alinhada.''',
'“Já tinha investido mais de R$40 mil reais em mentoria de marketing e o que resolveu minhas redes foi a experiência desse conteúdo novo que a Vanessa trouxe.”\nAndrea Spolaor','QUERO CRESCER LEVE'),
('Elaine','PSICÓLOGA','A candidíase que a acompanhou por 5 anos desapareceu após entender a decisão que precisava sustentar. Começou a cobrar mais e ter mais tempo livre.',
'''Uma história sobre dinheiro, escolhas e espaço para viver.

Elaine é psicóloga e especialista em Avaliação Psicológica.

Relatou que a experiência com o CSV contribuiu para trabalhar a relação com o próprio valor e decisões profissionais. Além de a ter livrado de uma candidíase que a acompanhava há 5 anos.

Ela já tinha 3 especializações quando sentia dificuldade em cobrar mais.

E agora cobra o valor justo pelo seu trabalho porque deixou para trás o bloqueio que atrapalhava a sustentar um valor mais alto.''',
'“Crescer também pode significar recuperar espaço na própria agenda.”\nElaine Cristina Mazaron','QUERO ME INSCREVER')]

learning_html = lines("""Porque ter conhecimento técnico não significa, necessariamente, saber transformá-lo em projetos e oportunidades.
O que pode estar acontecendo quando você sabe o que precisa fazer, mas continua adiando decisões importantes.
Como transformar sua experiência em novas entregas profissionais, sem precisar abandonar a atuação que já construiu.
Por que presença digital, posicionamento, vendas e sustentação emocional precisam funcionar juntos.
Como buscar uma expansão que não depende simplesmente de preencher mais horários na agenda.""")
qualification_html = lines("""Têm experiência, mas sentem que ainda podem ir além.
Guardam projetos que gostariam de finalmente realizar.
Querem comunicar melhor seu valor e vender com ética.
Já estudaram muito, mas precisam transformar conhecimento em ação.
Desejam ampliar suas oportunidades sem depender de mais horas de atendimento.
Querem crescer profissionalmente sem abrir mão da vida pessoal.""")
stories_html = ''.join(testimonial(*x) for x in stories)
reason_data = [
    ('Competência técnica ≠ competência comercial','Saber atender é diferente de saber estruturar, comunicar e vender novos serviços.'),
    ('A agenda tem limites','Se tudo depende de horas de atendimento, novas entregas podem ampliar possibilidades.'),
    ('Intenção não é execução','Ter vontade de fazer algo não garante que a ação aconteça.'),
    ('Valor precisa ser comunicado','Seu público não conhece automaticamente tudo o que você estudou e viveu.'),
    ('Crescer não precisa ser trabalhar sem parar','Tempo, energia e vida pessoal também precisam entrar nas decisões.'),
]
reasons_html = ''.join(f'<div class="reason"><span class="num">0{i}</span><div><h3>{e(t)}</h3><p>{e(b)}</p></div></div>' for i,(t,b) in enumerate(reason_data,1))
offer_items = ['1. O Comando da Sua Vida (CSV) — R$ 3.497','2. Energia Infinita — R$ 697','3. Intimidade Restaurada — R$ 697','4. Projeto Fora da Gaveta — Imersão online e ao vivo — R$ 997','5. Presença Digital — Imersão online e ao vivo — R$ 997','6. Conexão de Valor — Imersão online e ao vivo — R$ 997','7. 12 atendimentos em grupo do CSV — R$ 1.200','8. Guardião — Acompanhamento individualizado por WhatsApp — Valor incalculável','9. LABEX — Laboratório de Experimentações — Valor incalculável','10. Suporte para dúvidas operacionais por e-mail e WhatsApp — Valor incalculável']
offer_items_html = ''.join(f'<li>{e(x)}</li>' for x in offer_items)
vanessa_html = paras("""Vanessa construiu sua trajetória estudando o comportamento humano, desenvolvendo metodologias e criando experiências de aprendizagem.

Formada em Psicologia pela Universidade de São Paulo, concluiu seu doutorado na mesma instituição em 2016 e também possui formação em sexologia.

Foi uma das fundadoras de O Corpo Explica, projeto que alcançou mais de 40 mil alunos.

As empresas que fundou, consideradas em conjunto, alcançaram aproximadamente R$ 100 milhões em faturamento ao longo de suas trajetórias.

Desde 2017, ela acumula experiência prática no mercado digital, incluindo criação de métodos, formações, imersões presenciais e online, projetos comerciais e de comunicação entre eles, seu próprio programa de televisão.

Também investiu em sua formação empresarial e enfrentou, na prática, os desafios de construir e vender novas ofertas.

Vanessa conhece a diferença entre ter um conhecimento valioso e conseguir transformá-lo em um projeto que chega ao público.""")
neg_html = paras("""Neg construiu sua experiência profissional em ambientes nos quais liderança, consciência situacional e tomada de decisões sob pressão possuem importância fundamental.

Como instrutor de voo e formador de pilotos de combate, desenvolveu uma relação prática com processos de análise, decisão e resposta a situações complexas e rápidas.

Ao lado de Vanessa, participou do desenvolvimento do Comando da Sua Vida, integrando conhecimentos sobre comportamento humano e padrões automáticos de reação.

No Alicerce, sua experiência contribui especialmente para a dimensão das decisões, da percepção dos próprios comportamentos e da capacidade de agir.

São repertórios diferentes que se encontram em uma mesma proposta: compreender, decidir, construir e continuar avançando.""")

html_doc=f'''<style>{css}</style><main class="alicerce-page" id="alicerce-extraordinario">
<section class="section hero"><div class="wrap"><div><span class="kicker">ALICERCE DO EXTRAORDINÁRIO</span><h1>Transforme o conhecimento que você acumulou em novos projetos, posicionamento, clientes de valor sem precisar sacrificar a própria vida para crescer.</h1><ul class="promise-list"><li>Crie modelos de atendimento e entrega.</li><li>Amplie suas formas de atuação.</li><li>Divulgue seu trabalho.</li><li>Crie novas oportunidades de clientes e receita.</li></ul><p>ALICERCE DO EXTRAORDINÁRIO: Uma jornada para transformar anos de conhecimento e experiência na próxima grande expansão da sua carreira.</p></div><div class="hero-mark" aria-hidden="true"></div></div></section>
<section class="section dark"><div class="narrow"><h2 class="section-title">Você cuida de todo mundo, mas quem cuida de você, da sua carreira e dos seus sonhos?</h2><p class="section-sub">Assista e descubra como transformar o conhecimento que já possui em novas possibilidades profissionais.</p><div class="video-box"><div><span class="play">▶</span><strong>INSERIR VÍDEO ORIGINAL</strong></div></div><span class="kicker">NESTE VÍDEO, VOCÊ VAI ENTENDER:</span><ul class="learning">{learning_html}</ul><p class="summary">Você não precisa começar do zero.<br>Precisa descobrir como expandir a carreira que já construiu.</p>{actions('QUERO REALIZAR MEUS SONHOS',False)}</div></section>
<section class="section paper friction"><div class="wrap"><h2 class="section-title">VOCÊ LEVOU ANOS PARA CHEGAR ATÉ AQUI.</h2><p class="section-sub">Mas será que já explorou tudo o que sua experiência permite construir?<br>Você estudou, se dedicou, conquistou a confiança de clientes e pacientes e acumulou um conhecimento valioso.<br>Mas talvez exista algo que ainda não conseguiu colocar no mundo.</p><div class="grid grid-4">{card('01','PROJETOS NA GAVETA','Grupos, palestras, formações e imersões que continuam apenas no planejamento.','projetos')}{card('02','SEU VALOR POUCO COMUNICADO','Você sabe o quanto pode ajudar, mas nem sempre consegue mostrar isso ao público certo.','valor')}{card('03','DIFICULDADE PARA COBRAR','Você gostaria de valorizar melhor sua experiência, mas ainda sente insegurança ao apresentar seus preços.','cobranca')}{card('04','UMA AGENDA NO LIMITE','Para crescer no modelo atual, parece que você precisaria trabalhar cada vez mais horas.','agenda')}</div><div class="friction-transition"><strong>E se a próxima etapa da sua carreira não precisasse ser apenas uma versão mais cansativa da atual?</strong><br><br>Você não precisa desvalorizar o que já conquistou nem começar do zero.<br>Sua trajetória pode ser o alicerce de possibilidades que ainda não explorou.</div>{actions('QUERO VER POSSIBILIDADES',False)}</div></section>
<section class="section cream"><div class="narrow"><h2 class="section-title">PARA QUEM É O ALICERCE?<br>Você já construiu uma carreira.<br>Agora pode descobrir o que mais pode fazer com ela.</h2><p class="section-sub">O Alicerce é para profissionais do cuidado humano que:</p><ul class="qual-list">{qualification_html}</ul><p class="areas">PSICOLOGIA · TERAPIA · SAÚDE · BEM-ESTAR · EDUCAÇÃO · DESENVOLVIMENTO HUMANO</p><div class="ethical">Você não precisa começar do zero.<br>Sua experiência é o ponto de partida.<br>Uma jornada para profissionais que já possuem conhecimento e desejam ampliar suas possibilidades, respeitando suas qualificações e os limites éticos de atuação.</div>{actions('QUERO CRESCER COM QUALIDADE')}</div></section>
<section class="section dark journey"><div class="wrap"><span class="kicker">Como funciona o Alicerce do Extraordinário</span><h2 class="section-title">Do conhecimento que você já tem à carreira que ainda pode construir.</h2><p class="section-sub">Uma jornada que integra expansão profissional, sustentação emocional e qualidade de vida.</p><div class="grid grid-3">{card('ETAPA 01','DESTRAVAR','Desenvolva recursos para sair da intenção e entrar em ação.')}{card('ETAPA 02','CONSTRUIR','Transforme experiência em entregas, conexões e vendas.')}{card('ETAPA 03','SUSTENTAR','Cuide da energia, dos relacionamentos e da vida que deseja viver.')}</div></div></section>
<section class="section paper stage"><div class="wrap"><span class="kicker">ETAPA 01 / DESTRAVAR</span><h2 class="section-title">Você sabe o que fazer. Agora precisa conseguir fazer.</h2><p class="section-sub">Trabalhe padrões automáticos que podem interferir nas suas decisões, na exposição profissional e na execução de projetos.</p><div class="grid grid-3">{card('PROGRAMA COMPLETO','Comando da Sua Vida (CSV)','Conteúdos gravados e ferramentas práticas para reconhecer e trabalhar padrões automáticos de comportamento.','implementacao')}{card('ENCONTROS MENSAIS','12 atendimentos em grupo','Aprofunde a aplicação do CSV, esclareça dúvidas e receba direcionamentos personalizados durante os encontros.','grupo')}{card('ACOMPANHAMENTO','Guardião','Orientação individualizada pelo WhatsApp com uma pessoa treinada da equipe.','agenda')}</div></div></section>
<section class="section paper stage"><div class="wrap"><span class="kicker">ETAPA 02 / CONSTRUIR</span><h2 class="section-title">Seu conhecimento pode se transformar em novas oportunidades.</h2><p class="section-sub">Três imersões online e ao vivo para transformar suas ideias em entregas profissionais, desenvolver conexões e fechar com novos clientes de valor.</p><div class="grid grid-3">{card('ENTREGA · JANEIRO 2027','Projeto Fora da Gaveta','Estruture grupos, workshops, formações, serviços ou outros projetos com foco na qualidade da entrega.','projetos')}{card('CONEXÃO · FEVEREIRO 2027','Presença Digital','Desenvolva posicionamento e comunicação para mostrar seu valor e se conectar com o público certo.','valor')}{card('VENDA · MARÇO 2027','Conexão de Valor','Aprenda a apresentar ofertas, conversar sobre preços e conduzir vendas com ética e segurança.','cobranca')}</div><p class="note">Imersões previstas para sábados inteiros, no final de janeiro, fevereiro e março de 2027.</p></div></section>
<section class="section dark stage"><div class="wrap"><span class="kicker">ETAPA 03 / SUSTENTAR</span><h2 class="section-title">Cresça profissionalmente sem deixar sua vida para depois.</h2><p class="section-sub">Porque uma carreira extraordinária também precisa fazer sentido para quem a vive.</p><div class="grid grid-3">{card('ENERGIA E PRAZER','Energia Infinita','Conteúdos e exercícios para trabalhar disposição, motivação, prazer e energia de vida.','energia')}{card('AUTOESTIMA E INTIMIDADE','Intimidade Restaurada','Trabalhe sua relação com o corpo, a autoestima, a sexualidade e a intimidade com privacidade.','intimidade')}{card('PRÁTICA E RELACIONAMENTOS','LABEX','Laboratório de Experimentações no Telegram para praticar comunicação, convivência e relacionamentos.','labex')}</div><p class="summary">Destravar para agir. Construir para expandir. Sustentar para viver.<br>Uma jornada integrada para transformar sua experiência em novas possibilidades profissionais e pessoais.</p>{actions('EU QUERO TUDO ISSO')}</div></section>
<section class="section paper stories"><div class="wrap"><h2 class="section-title">HISTÓRIAS REAIS</h2>{stories_html}</div></section>
<section class="section cream execution"><div class="wrap"><span class="kicker">JORNADA · EXECUÇÃO E ACOMPANHAMENTO</span><h2 class="section-title">Muito além de assistir a aulas</h2><p class="section-sub">Conteúdos gravados, ferramentas práticas, exercícios corporais, imersões ao vivo, atendimentos em grupo e acompanhamento em uma jornada integrada.</p><div class="grid grid-3">{card('06 MESES','Implementação acompanhada','Com calendário sugerido para aplicar os conteúdos que já estão gravados.','implementacao')}{card('12 MESES','Acesso aos conteúdos','Para estudar, revisar e retomar os materiais.','acesso')}{card('03 IMERSÕES PRÁTICAS','Sábados inteiros, online e ao vivo','Com espaço para dúvidas e gravações para reassistir quando quiser.','imersoes')}{card('12 ENCONTROS CSV','Atendimentos em grupo mensais','Para aplicação e aprofundamento do método.','grupo')}{card('WHATSAPP E E-MAIL','Guardião da jornada','Guardião da jornada e Suporte operacional pelo WhatsApp individual com pessoa treinada da equipe.','whatsapp')}{card('COMUNIDADE','Labex','Comunidade no Telegram para praticar comunicação, convivência e relacionamentos.','labex_oficial')}</div><p class="quote">“A jornada tem uma sequência. Mas o seu ritmo e a sua trajetória também importam.”</p>{actions('QUERO ME INSCREVER')}</div></section>
<section class="section paper"><div class="narrow"><span class="kicker">GARANTIAS · SEGURANÇA DE DECISÃO</span><h2 class="section-title">Duas garantias para sua decisão</h2><div class="grid grid-2"><article class="guarantee"><h3>7 DIAS INCONDICIONAIS</h3><p>Solicite cancelamento e devolução no prazo previsto, por qualquer motivo que desejar.</p></article><article class="guarantee"><h3>6 MESES · GARANTIA PRÁTICA</h3><p>Implemente o processo proposto e se não alcançar resultado algum na expansão profissional, poderá solicitar a devolução integral.</p></article></div>{actions('CLIQUE E SE INSCREVA')}</div></section>
<section class="section cream creators"><div class="wrap"><h2 class="section-title">Quem criou o Alicerce do Extraordinário?</h2><p class="section-sub">Duas experiências complementares. Uma jornada construída para transformar conhecimento em ação.</p><div class="grid grid-2"><article class="creator"><div class="creator-photo">{img('vanessa','Dra. Vanessa Cesnik sorrindo')}</div><div class="creator-body"><span class="eyebrow">Psicóloga, doutora em Psicologia pela USP, pesquisadora e empresária</span><h3>DRA. VANESSA CESNIK</h3>{vanessa_html}</div></article><article class="creator"><div class="creator-photo">{img('neg','Neg Negreiros sorrindo')}</div><div class="creator-body"><span class="eyebrow">Coronel do Exército, instrutor de piloto de combate e cofundador da Realizando Potenciais</span><h3>NEG NEGREIROS</h3>{neg_html}</div></article></div>{actions('APRENDER NA PRÁTICA')}</div></section>
<section class="section paper reasons"><div class="narrow"><span class="kicker">RAZÃO PARA AGIR</span><h2 class="section-title">Seu conhecimento tem valor. Mas ele não se transforma sozinho em oportunidades.</h2>{reasons_html}{actions('CRESCER COM QUALIDADE')}</div></section>
<section class="section offer"><div class="narrow"><span class="kicker">BLACK NOVEMBER</span><h2 class="section-title">Tudo o que você recebe na Black November</h2><p class="section-sub">Uma experiência integrada, organizada em três movimentos.</p><div class="offer-table"><h3>Quanto custaria pra comprar separado?</h3><ol class="offer-list">{offer_items_html}</ol><div class="anchor">VALOR TOTAL SE FOSSE COMPRAR SEPARADO<span class="old">R$ 9.082</span></div></div><div class="price-box"><span class="deadline">CONDIÇÃO DE ABERTURA ATÉ 06/11 23h59</span><div class="discount">72,5% de desconto</div><div class="price">12× DE R$ 247,83</div><div class="cash">ou R$ 2.497 à vista</div>{actions('SE INSCREVER AGORA',False)}</div></div></section>
<footer class="section footer"><div class="wrap"><div>Copyright © Realizando Potenciais</div><div class="legal">PoLitica de Privacidade | Termos de Uso</div><p class="disclaimer">Este conteúdo tem fins educativos e utiliza princípios da Psicologia e neurociência baseados em evidências para promover autorreflexão e bem-estar emocional. Não substitui acompanhamento médico ou psicológico. Os resultados obtidos com o método CSV variam de pessoa para pessoa. Eles dependem de múltiplos fatores, como histórico pessoal, perfil emocional, contexto de vida atual e nível de envolvimento com as práticas propostas. As informações listadas nesta página representam possibilidades de desenvolvimento pessoal, e não garantias de resultado.</p></div></footer>
</main>'''

(OUT_DIR/'alicerce-page.html').write_text(html_doc,encoding='utf-8')
# Local-only QA preview: same markup/CSS, with local copies of the approved assets.
import shutil
qa_assets = OUT_DIR / 'assets'
qa_assets.mkdir(exist_ok=True)
source_paths = {
    'projetos': ASSET_DIR / 'pexels-19905182-projetos.jpg',
    'valor': ASSET_DIR / 'pexels-34086093-valor.jpg',
    'cobranca': ASSET_DIR / 'pexels-7688187-cobranca.jpg',
    'agenda': ASSET_DIR / 'pexels-8646391-agenda.jpg',
    'implementacao': ASSET_DIR / 'pexels-5905852-implementacao.jpg',
    'imersoes': ASSET_DIR / 'pexels-18999470-imersoes.jpg',
    'acesso': ASSET_DIR / 'pexels-1558691-acesso-anual.jpg',
    'energia': ASSET_DIR / 'pexels-10057634-energia.jpg',
    'intimidade': ASSET_DIR / 'pexels-34436646-intimidade.jpg',
    'labex': ASSET_DIR / 'pexels-19895721-labex.jpg',
    'vanessa': ASSET_DIR / 'vanessa-BCK_9101-sorrindo.jpg',
    'neg': ASSET_DIR / 'neg-IMG_8303-sorrindo.jpg',
    'grupo': EXEC_DIR / '1.jpeg',
    'whatsapp': EXEC_DIR / '4.png',
    'labex_oficial': EXEC_DIR / '3.jpeg',
}
preview_doc = html_doc
for key, source in source_paths.items():
    target_name = f'{key}{source.suffix.lower()}'
    shutil.copy2(source, qa_assets / target_name)
    preview_doc = preview_doc.replace(U[key], f'assets/{target_name}')
(OUT_DIR/'preview.html').write_text('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Alicerce do Extraordinário — Preview</title></head><body style="margin:0">'+preview_doc+'</body></html>',encoding='utf-8')
print(json.dumps({'html_path':str(OUT_DIR/'alicerce-page.html'),'preview_path':str(OUT_DIR/'preview.html'),'chars':len(html_doc)},ensure_ascii=False))
