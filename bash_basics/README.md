# <img height="32px" align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg"/>&nbsp;**Bash&nbsp;basics**

Comandos básicos para utilização do bash.

## **Navegação:**

- **_`cd`_**: '**c**hange **d**irectory' / Mudar diretório

  Usado para navegar entre as diferentes pastas e subpastas do sistema. Exemplos:

  - Navegar até a pasta raiz do usuário:

    ```sh
    cd ~ # **Obs:** o '~' é usado para indicar a raiz do usuário logado
    ```

  - Entrar e voltar de uma pasta chamada 'pasta':

    ```sh
    cd pasta # entra na pasta indicada
    cd .. # volta para a pasta anterior
    ```

    **Obs:** Em um terminal _bashLike_ existem duas pastas por padrão em cada diretório.
    As pastas '.' e '..', as quais indicam, respectivamente, a pasta atual e a
    pasta anterior (pasta mãe/pai).

- **_`ls`_**: '**l**i**s**t directory' / Listar diretório

  Usado para listar os arquivos e pastas na pasta atual. Exemplos:

  - Listar os arquivos e diretórios da pasta atual:

    ```sh
    ls .
    ```

  - Listar os arquivos e diretórios ocultos da pasta atual:

    ```sh
    ls . -a # o '-a' é equivalente à '--all' / todos
    ```

    **Obs:** Em um terminal _bashLike_ os arquivos/pastas ocultos(as) são indicadas
    com um ponto no início do nome. Exemplos: .git, .bashrc, .cache.

  - Listar os arquivos/diretórios da pasta atual com mais informações sobre eles:

    ```sh
    ls . -l # -l indica list/lista (nesse caso não existe o parâmetro '--list')
    ```

    **Obs1:** algumas informações úteis sobre os arquivos/diretórios mostradas
    nessa visualização: permissões, usuário criador, tamanho (em bytes) e ultima
    atualização.

    **Obs2:** Em um terminal _bashLike_ você pode combinar parâmetros em um único
    comando, sendo possível rodar, por exemplo, `ls -la` para listar todos os
    arquivos com informações adicionais.

## **Arquivos e Diretórios:**

- **_`mkdir`_**: '**m**a**k**e **dir**ectory' / Criar diretório

  Cria um diretório na pasta atual. Exemplo:
  
  - Criar uma pasta chamada 'teste' na pasta atual:

    ```sh
    mkdir teste
    ```

- **_`touch`_**: Tocar, triscar

  Cria um arquivo com o nome e a extensão indicada. Exemplos:

  - Criar arquivo 'teste.txt' na pasta atual:

    ```sh
    touch teste.txt
    ```

  - Criar um arquivo oculto com nome 'oculto.txt' na pasta atual:

    ```sh
    touch .oculto.txt
    ```

- **_`nano`_**, **_`vim`_**:

  Ambos são editores de arquivo e podem ser abertos utilizando o comando seguido
  do nome do arquivo.
