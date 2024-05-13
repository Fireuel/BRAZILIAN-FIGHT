import streamlit as st

personagens = {
    "SACI": "No coração das densas florestas do Brasil, entre árvores centenárias e segredos antigos, vive uma figura lendária conhecida como Saci. Este ser travesso e misterioso é retratado como um menino negro de uma perna só, sempre vestindo um gorro vermelho e fumando seu inseparável cachimbo.\nO gorro vermelho do Saci concede a ele poderes mágicos únicos. Podendo se transformar em um redemoinho de vento além de desaparecer no ar. Podendo até usar sua magia para confundir e desorientar seus adversários, criando ilusões e manipulando o ambiente ao seu redor.",

    "CURUPIRA": "Um anão forte e ágil com seus cabelos vermelhos de fogo e seus pés virados para trás, ele é uma figura mítica e imponente nos campos de batalha.\nEle pode invocar criaturas da floresta para ajudá-lo em combate, manipular o ambiente ao seu redor e até mesmo controlar o próprio fogo, transformando-o em uma arma poderosa contra seus inimigos",

    "LOBISOMEM": "É uma criatura híbrida (animal proveniente de duas espécies diferentes), meio homem, meio lobo, cuja transformação é desencadeada pelos raios prateados da lua cheia. Nesse estado selvagem, ele perde o controle sobre sua humanidade, entregando-se aos instintos predatórios e à fúria incontrolável.\nPossui uma grande velocidade, saltar muito alto, podendo atacar com um golpe devastador, derrubando ou lançando seus oponentes para longe.",

    "IARA": "A Iara, também conhecida como Mãe d'Água Ela é protetora das águas e de seus habitantes, mas também pode se tornar vingativa e impiedosa com aqueles que a desrespeitam ou atraem sua ira. sua beleza hipnotizante é apenas uma fachada para sua verdadeira natureza feroz e implacável.\nCom longos cabelos negros como a noite e olhos hipnotizantes ela é conhecida por sua voz melodiosa e sua capacidade de atrair os homens para as profundezas das águas, onde são seduzidos e nunca mais retornam.",

    "JACI": "Tem com sua origem uma jovem guerreira destemida e habilidosa, nascida sob a luz prateada da Lua. Criada por uma tribo ancestral (Filha de Tupã), guardiã da noite e personificação da Lua. Ela também é responsável por proteger as plantas. Guardiã da noite, a deusa Jaci é considerada a personificação da Lua. Ela é responsável por proteger as plantas e cuidar da noite.\nPodendo convocar criaturas da noite, como corujas, lobos ou morcegos, para ajudá-la em batalha, atacando os inimigos ou fornecendo suporte tático.",

    "ZUMBI DOS PALMARES": "Personagem  ícone da resistência negra à escravidão, liderou o Quilombo dos Palmares, comunidade livre formada por escravos fugitivos das fazendas no Brasil Colonial.\nPara atacar ele usa chutes inspirados na capoeira. Sendo golpes ágeis e imprevisíveis permitindo que surpreendam seus oponentes.",

    "DANDARA": "Dandara dos Palmares foi uma guerreira negra do período colonial do Brasil no Quilombo de Palmares. Zumbi dos Palmares teve 3 filhos, ela lutou com armas pela libertação total das negras e negros no Brasil, liderava mulheres e homens, além que ajudava na manutenção do quilombo, trabalhando nas colheitas e na caça.\nEmpunhando uma lança, Dandara avança contra seus inimigos com uma serie de golpes rápidos.",

    "TIRADENTES": "Joaquim José da Silva Xavier, mais conhecido como Tiradentes, foi um dentista, tropeiro, minerador e comerciante. Nascido em Minas Gerais durante o período colonial do Brasil,  realizou o cargo  como alferes (antigo posto militar, equivalente ao atual de segundo-tenente). Movido por um senso de justiça e liberdade, ele se uniu a outros visionários em busca de um Brasil livre e independente do governo colonial português sobre o povo brasileiro.\nTiradentes desfere um soco poderoso carregado com toda a sua determinação e vontade de liberdade, causando sérios danos ao seu oponente.",

    "DOM PEDRO I": "Dom Pedro I (Filho de d. João VI, rei de Portugal, é um dos grandes nomes da história do Brasil. Foi um dos condutores do processo de independência  no Brasil, em 7 de setembro de 1822, às margens do rio Ipiranga, ele proclamou a independência do país, declarando-se o primeiro imperador do país.\nUtilizando uma espada Dom Pedro realiza golpes rápidos e precisos, demonstrando sua habilidade como comandante militar e sua determinação em proteger a nação.",

    "IRMÃ DULCE": "Maria Rita de Souza Brito Lopes, a Irmã Dulce, acolhia pessoas carentes em seu próprio lar, aos 13 anos, já ajudava os mendigos e doentes que encontrava nas ruas da cidade. Ingressou na Congregação das Irmãs Missionárias da Imaculada Conceição da Mãe de Deus, onde assumiu o nome de Irmã Dulce em homenagem à sua mãe. Ela dedicou sua vida ao serviço dos mais necessitados, especialmente dos pobres, doentes e desabrigados.\nIrmã Dulce estende a mão em direção ao oponente, emitindo uma que causa dano aos seus oponentes.",
}

def exibir_historia(personagem): #aqui é a função que puxa a história do personagem pelo nome dele lá na list
    if personagem in personagens:
        st.write(f"**História de {personagem}:**")
        st.write(personagens[personagem])
    else:
        st.write("Personagem não encontrado. Escolha um dos personagens disponíveis.")

def main():
    st.title("História de cada personagem") #título da pág
    st.write("Escolha um personagem para ver sua história:") #uma frase informativa só pra ter

    col1, col2 = st.columns(2) #isso aqui divide a tela em duas colunas

    for nome_personagem in list(personagens.keys())[:5]: #aqui cria os 5 primeiros botões lá da list
        if col1.button(nome_personagem):
            exibir_historia(nome_personagem)

    for nome_personagem in list(personagens.keys())[5:]: #5 últimos botões da lista
        if col2.button(nome_personagem):
            exibir_historia(nome_personagem)
        
if __name__ == "__main__":
    main()