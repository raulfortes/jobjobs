-----
PiP
-----
1. Instalar pip

Somente caso não tenho o pip ainda

::

    sudo easy_install pip

---------------

VIrtualEnv
-----
1. Instalar o Virtual Envoriment Wrapper

Instalar o Virtual Wrapper para facilitar o uso de virtualenv

::

    sudo pip install virtualenvwrapper

2. Adicionar ao bash_profile

::

    echo '. /usr/local/bin/virtualenvwrapper.sh' >> ~/.bash_profile

3. Update bash_profile

Para garantir que o virtualenvwrapper está rodando

::

    . ~/.bash_profile

4. Virtual Envoriment jobjobs

Para Criar

::

    mkvirtualenv jobjobs

Para utilizar um já existente

::

    workon jobjobs

5. Dependências

Baixar todas as dependências do projeto pelo pip para o virtualenv em uso

::

    pip install -r ~/jobjobs/docs/pip-requirements.txt 

---------------

Run
-----
1. Executar run.py

::

    python ~/jobjobs/src/main/python/c2f/run.py

---------------