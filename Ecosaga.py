import pygame
import sys

pygame.init()
pygame.mixer.init()


# Tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("ECOSAGA")

# Cores
BRANCO = (255, 255, 255)
CINZA = (200, 200, 200)
VERDE = (0, 150, 0)
VERDE_ESCURO = (0, 100, 0)
PRETO = (0, 0, 0)
VERMELHO = (200, 0, 0)

# Fontes
fonte_titulo = pygame.font.SysFont("arialblack", 54)
fonte_info = pygame.font.SysFont("arial", 32)
fonte_pequena = pygame.font.SysFont("arial", 24)

# Imagens
def carregar_imagem(caminho, tamanho=None):
    try:
        img = pygame.image.load(caminho).convert_alpha()
        if tamanho:
            img = pygame.transform.scale(img, tamanho)
        return img
    except:
        return None

capa = carregar_imagem("CAPA OFICIAL JOGO ECOSAGA (1) (1).png", (800, 600))
icone_voltar_img = carregar_imagem("Seta Retro em Pixels.png", (40, 40))
icone_modo_img = carregar_imagem("Engrenagem Dourada Pixelada.png", (40, 40))
imagem_inimigo = pygame.image.load("inimigos.png").convert_alpha()
imagem_chefe = pygame.image.load("chefe.png").convert_alpha()

imagem_inimigo = pygame.transform.scale(imagem_inimigo, (60, 80))
imagem_chefe = pygame.transform.scale(imagem_chefe, (80, 100))



def desenhar_botao(texto, x, y, largura, altura, cor, cor_hover, mouse_pos):
    if x < mouse_pos[0] < x + largura and y < mouse_pos[1] < y + altura:
        pygame.draw.rect(tela, cor_hover, (x, y, largura, altura), border_radius=12)
    else:
        pygame.draw.rect(tela, cor, (x, y, largura, altura), border_radius=12)
    texto_render = fonte_info.render(texto, True, BRANCO)
    tela.blit(texto_render, (x + (largura - texto_render.get_width()) // 2,
                             y + (altura - texto_render.get_height()) // 2))
    return pygame.Rect(x, y, largura, altura)

def tela_vitoria():
    while True:
        tela.fill(VERDE_ESCURO)
        texto = fonte_titulo.render("VITÓRIA!", True, BRANCO)
        sub = fonte_info.render("Parabéns, você salvou a floresta!", True, BRANCO)
        voltar = fonte_pequena.render("Clique para retornar ao menu", True, CINZA)
        tela.blit(texto, ((LARGURA - texto.get_width()) // 2, 180))
        tela.blit(sub, ((LARGURA - sub.get_width()) // 2, 260))
        tela.blit(voltar, ((LARGURA - voltar.get_width()) // 2, 350))
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                return

def tela_inicial():
    while True:
        tela.fill((34, 139, 34))
        mouse_pos = pygame.mouse.get_pos()

        if capa:
            tela.blit(capa, ((LARGURA - capa.get_width()) // 2, 1))
        else:
            titulo = fonte_titulo.render("ECOSAGA", True, BRANCO)
            tela.blit(titulo, ((LARGURA - titulo.get_width()) // 2, 50))

        botao_continuar = desenhar_botao("Iniciar", 300, 450, 200, 50, VERDE_ESCURO, (0, 200, 0), mouse_pos)
        botao_sair = desenhar_botao("X", 745, 10, 50, 50, VERMELHO, (255, 0, 0), mouse_pos)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_continuar.collidepoint(evento.pos):
                    return
                if botao_sair.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

def tela_nome_usuario():
    usuario = ""
    input_ativo = False

    # Carregar o fundo de floresta pixel
    try:
        fundo_floresta = pygame.image.load("fundo_floresta.png").convert()
        fundo_floresta = pygame.transform.scale(fundo_floresta, (LARGURA, ALTURA))
    except:
        fundo_floresta = None

    while True:
        if fundo_floresta:
            tela.blit(fundo_floresta, (0, 0))
        else:
            tela.fill(VERDE)

        mouse_pos = pygame.mouse.get_pos()

        instrucao = fonte_info.render("Digite seu nome de usuário:", True, BRANCO)
        tela.blit(instrucao, ((LARGURA - instrucao.get_width()) // 2, 200))

        caixa_input = pygame.Rect(250, 250, 300, 40)
        pygame.draw.rect(tela, BRANCO if input_ativo else CINZA, caixa_input, border_radius=15, width=2)
        texto_usuario = fonte_info.render(usuario, True, BRANCO)
        tela.blit(texto_usuario, (260, 250))

        botao_continuar = desenhar_botao("Continuar", 300, 320, 200, 50, VERDE_ESCURO, (0, 200, 0), mouse_pos)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if caixa_input.collidepoint(evento.pos):
                    input_ativo = True
                else:
                    input_ativo = False
                if botao_continuar.collidepoint(evento.pos) and usuario.strip():
                    return usuario
            if evento.type == pygame.KEYDOWN and input_ativo:
                if evento.key == pygame.K_BACKSPACE:
                    usuario = usuario[:-1]
                elif len(usuario) < 20:
                    usuario += evento.unicode

def menu_personagem():
    modo_automatico = False

    try:
        fundo_personagem = pygame.image.load("Selecione o Seu Personagem.png").convert()
        fundo_personagem = pygame.transform.scale(fundo_personagem, (LARGURA, ALTURA))
    except:
        fundo_personagem = None

    personagem1 = pygame.image.load("personagem masculino.png").convert_alpha()
    personagem2 = pygame.image.load("personagem feminina.png").convert_alpha()

    personagem1 = pygame.transform.scale(personagem1, (160, 160))
    personagem2 = pygame.transform.scale(personagem2, (180, 180))




    while True:
        if fundo_personagem:
            tela.blit(fundo_personagem, (0, 0))
        else:
            tela.fill(VERDE)

        mouse_pos = pygame.mouse.get_pos()

        x1, y1 = 200, 200
        x2, y2 = 500, 200
        tela.blit(personagem1, (x1, y1))
        tela.blit(personagem2, (x2, y2))

        nome1 = fonte_pequena.render("Personagem 1", True, BRANCO)
        nome2 = fonte_pequena.render("Personagem 2", True, BRANCO)
        tela.blit(nome1, (x1 + 10, y1 - 30))
        tela.blit(nome2, (x2 + 10, y2 - 30))

        largura_botao, altura_botao = 100, 40
        botao_personagem1 = pygame.Rect(x1, y1 + 165, largura_botao, altura_botao)
        botao_personagem2 = pygame.Rect(x2, y2 + 165, largura_botao, altura_botao)

        def desenhar_botao_personagem(botao, texto):
            cor = VERDE_ESCURO if not botao.collidepoint(mouse_pos) else (0, 200, 0)
            pygame.draw.rect(tela, cor, botao, border_radius=8)
            texto_render = fonte_pequena.render(texto, True, BRANCO)
            tela.blit(texto_render, (botao.x + (botao.width - texto_render.get_width()) // 2,
                                     botao.y + (botao.height - texto_render.get_height()) // 2))

        desenhar_botao_personagem(botao_personagem1, "Escolher")
        desenhar_botao_personagem(botao_personagem2, "Escolher")

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_personagem1.collidepoint(evento.pos):
                    return personagem1, modo_automatico
                if botao_personagem2.collidepoint(evento.pos):
                    return personagem2, modo_automatico


def carregar_frames(sprite_sheet):
    frame_largura = sprite_sheet.get_width() // 4
    frame_altura = sprite_sheet.get_height() // 2
    frames_direita, frames_esquerda = [], []

    for linha in range(2):
        for coluna in range(4):
            frame = sprite_sheet.subsurface((coluna * frame_largura, linha * frame_altura, frame_largura, frame_altura))
            frame = pygame.transform.scale(frame, (75, 90))
            frames_direita.append(frame)
            frames_esquerda.append(pygame.transform.flip(frame, True, False))

    return frames_direita, frames_esquerda

class Inimigo:
    def __init__(self, x, y, velocidade):
        self.x = x
        self.y = y
        self.largura = 50
        self.altura = 70
        self.velocidade = velocidade
        self.cor = (200, 50, 50)
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.passou = False
        self.vivo = True

    def mover(self):
        self.x -= self.velocidade
        if self.x < -self.largura:
            self.x = LARGURA + 100
            self.passou = False
        self.rect.x = self.x

    def desenhar(self, surface):
        if self.vivo:
           surface.blit(imagem_inimigo, self.rect)

def tela_game_over():
    while True:
        tela.fill(PRETO)
        texto = fonte_titulo.render("GAME OVER", True, VERMELHO)
        sub = fonte_info.render("Clique para retornar ao menu", True, BRANCO)
        tela.blit(texto, ((LARGURA - texto.get_width()) // 2, 200))
        tela.blit(sub, ((LARGURA - sub.get_width()) // 2, 300))
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                return

class Chefe:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = 80
        self.altura = 100
        self.vidas = 5
        self.velocidade = 2
        self.cor = (150, 0, 150)
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.vivo = True

    def mover(self):
        self.x -= self.velocidade
        self.rect.x = self.x
        

    def desenhar(self, surface):
        if self.vivo:
            surface.blit(imagem_chefe, self.rect)
            barra = pygame.Rect(self.rect.x, self.rect.y - 10, self.largura, 5)
            pygame.draw.rect(surface, VERMELHO, barra)
            pygame.draw.rect(surface, VERDE, (self.rect.x, self.rect.y - 10, self.largura * (self.vidas / 5), 5))

def iniciar_jogo(usuario, sprite_sheet, modo_automatico):
    pygame.mixer.music.load("pixel-fight-8-bit-arcade-music-background-music-for-video-208775.mp3")  # Caminho para sua música
    pygame.mixer.music.set_volume(0.3)  # Volume de 0.0 a 1.0
    pygame.mixer.music.play(-1)  # -1 faz a música tocar em loop infinito
    som_pulo = pygame.mixer.Sound("cartoon-jump-6462.mp3")
    som_pulo.set_volume(0.5)  # Ajuste o volume se necessário
    som_coin = pygame.mixer.Sound("coin-collision-sound-342335.mp3")
    som_coin.set_volume(1.0)


    fundo = carregar_imagem("fundo do jogo.png", (1600, ALTURA))
    largura_fundo = fundo.get_width()
    sprite_sheet = sprite_sheet.convert_alpha()
    frames_direita, frames_esquerda = carregar_frames(sprite_sheet)

    personagem_rect = pygame.Rect(100, 400, 75, 90)
    frame_index, tempo_animacao, ultimo_update = 0, 100, pygame.time.get_ticks()
    direcao, velocidade, gravity, vel_y = "direita", 5, 0.8, 0
    no_chao, chao_y, camera_x = True, 400, 0
    clock = pygame.time.Clock()
    vida_maxima, vida_atual, pontos = 100, 100, 0

    inimigos = []
    tempo_ultimo_spawn = pygame.time.get_ticks()
    intervalo_spawn = 2000
    velocidade_inicial_inimigo = 1.5
    velocidade_atual_inimigo = velocidade_inicial_inimigo

    chefe = None
    alerta_ativo = False
    tempo_alerta = 0

    while True:
        clock.tick(60)
        mouse_pos = pygame.mouse.get_pos()
        voltar_rect = pygame.Rect(LARGURA - 60, 10, 40, 40)
        modo_rect = pygame.Rect(LARGURA - 110, 10, 40, 40)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if voltar_rect.collidepoint(evento.pos):
                    return
                elif modo_rect.collidepoint(evento.pos):
                    modo_automatico = not modo_automatico

        teclas = pygame.key.get_pressed()
        andando = False

        if modo_automatico:
            personagem_rect.x += velocidade
            camera_x += velocidade
            direcao = "direita"
            andando = True
        else:
            if teclas[pygame.K_LEFT]:
                personagem_rect.x -= velocidade
                camera_x -= velocidade
                direcao = "esquerda"
                andando = True
            if teclas[pygame.K_RIGHT]:
                personagem_rect.x += velocidade
                camera_x += velocidade
                direcao = "direita"
                andando = True

        if teclas[pygame.K_SPACE] and no_chao:
            vel_y = -15
            no_chao = False
            som_pulo.play()

        vel_y += gravity
        personagem_rect.y += vel_y
        if personagem_rect.y >= chao_y:
            personagem_rect.y = chao_y
            vel_y = 0
            no_chao = True

        tempo_atual = pygame.time.get_ticks()
        if andando and tempo_atual - ultimo_update > tempo_animacao:
            frame_index = (frame_index + 1) % len(frames_direita)
            ultimo_update = tempo_atual
        elif not andando:
            frame_index = 0

        frame_atual = frames_direita[frame_index] if direcao == "direita" else frames_esquerda[frame_index]

        for i in range(-1, LARGURA // largura_fundo + 3):
            tela.blit(fundo, ((i * largura_fundo) - (camera_x % largura_fundo), 0))

        # Alerta de chefe
        if pontos > 0 and pontos % 20 == 0 and chefe is None and not alerta_ativo:
            alerta_ativo = True
            tempo_alerta = tempo_atual

        if alerta_ativo:
            texto_alerta = fonte_info.render(" !!!CHEFE SE APROXIMANDO!!! ", True, VERMELHO)
            tela.blit(texto_alerta, ((LARGURA - texto_alerta.get_width()) // 2, 100))
            if tempo_atual - tempo_alerta > 2000:
                chefe = Chefe(LARGURA + 50, chao_y)
                alerta_ativo = False

        if chefe and chefe.vivo:
            chefe.mover()
            
            if chefe.x + chefe.largura < 0:
                pygame.mixer.music.stop()  
                tela_game_over()           
                return                    
            
            chefe.desenhar(tela)
            if personagem_rect.colliderect(chefe.rect):
                if personagem_rect.bottom <= chefe.rect.top + 10 and vel_y > 0:
                    chefe.vidas -= 1
                    vel_y = -10
                    if chefe.vidas <= 0:
                        chefe.vivo = False
                        chefe = None
                        velocidade_atual_inimigo += 1
                        pontos += 3
                        som_coin.play()
                    
                else:
                    vida_atual -= 1
                    vida_atual = max(0, vida_atual)
                    
        else:
            if tempo_atual - tempo_ultimo_spawn > intervalo_spawn:
                inimigos.append(Inimigo(LARGURA + 100, chao_y + 10, velocidade_atual_inimigo))
                tempo_ultimo_spawn = tempo_atual

            for inimigo in inimigos[:]:
                if inimigo.vivo:
                    inimigo.mover()
                    if personagem_rect.colliderect(inimigo.rect):
                        if personagem_rect.bottom <= inimigo.rect.top + 10 and vel_y > 0:
                            inimigo.vivo = False
                            vel_y = -10
                            pontos += 1
                            som_coin.play()
                        else:
                            vida_atual -= 1
                            vida_atual = max(0, vida_atual)
                    inimigo.desenhar(tela)
                else:
                    if inimigo.x < -inimigo.largura:
                        inimigos.remove(inimigo)
        
        nome_render = fonte_pequena.render(f"Jogador: {usuario}", True, BRANCO)
        tela.blit(nome_render, (10, 10))           

        if vida_atual <= 0:
            tela_game_over()
            return

        if pontos >= 60:
            tela_vitoria()
            return
        

        tela.blit(frame_atual, personagem_rect)

        proporcao = vida_atual / vida_maxima
        pygame.draw.rect(tela, VERMELHO, (10, 50, 200, 20))
        pygame.draw.rect(tela, VERDE, (10, 50, 200 * proporcao, 20))
        pygame.draw.rect(tela, BRANCO, (10, 50, 200, 20), 2)

        texto_pontos = fonte_pequena.render(f"Pontos: {pontos}", True, BRANCO)
        tela.blit(texto_pontos, (LARGURA - texto_pontos.get_width() - 10, 50))

        tela.blit(icone_voltar_img, voltar_rect) if icone_voltar_img else pygame.draw.rect(tela, CINZA, voltar_rect)
        tela.blit(icone_modo_img, modo_rect) if icone_modo_img else pygame.draw.rect(tela, CINZA, modo_rect)

        pygame.display.update()
pygame.mixer.music.stop()


# Fluxo principal
while True:
    tela_inicial()
    usuario = tela_nome_usuario()
    sprite_sheet, modo_automatico = menu_personagem()
    iniciar_jogo(usuario, sprite_sheet, modo_automatico)
    