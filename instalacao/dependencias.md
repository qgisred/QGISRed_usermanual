#Gerenciamento de Dependências

QGISRed precisa de um conjunto de bibliotecas de cálculo externas **(dependências do plugin QGISRed)** para poder executar a maioria de suas ferramentas. Estas bibliotecas são DLLs compiladas em .NET que contêm o motor hidráulico (baseado no kit de ferramentas EPANET 2.3) e os algoritmos de processamento geoespacial.

---

## Primeira instalação

Na primeira vez que você tenta usar qualquer ferramenta QGISRed, o plugin detecta que as dependências não estão instaladas e exibe uma caixa de diálogo de confirmação:

<figure><img src="../assets/images/instalacion/dialogo-dependencias.png" alt="Caixa de diálogo de instalação de dependência"><figcaption><p>QGISRed solicita permissão para baixar as dependências.</p></figcaption></figure>

- **Sim**: QGISRed baixa e instala as bibliotecas automaticamente. O download requer conexão com a internet e pode demorar alguns segundos dependendo da velocidade da conexão.
- **Não**: a ferramenta não é executada. A caixa de diálogo aparecerá novamente na próxima vez que você tentar usar o plugin.

> A instalação **não requer permissões de administrador**. As DLLs são instaladas na pasta do usuário `%APPDATA%\QGISRed\`, não nas pastas do sistema.

---

## Onde eles estão instalados

As dependências são armazenadas em:

```
C:\Users\{tu_usuario}\AppData\Roaming\QGISRed\
```

Você pode acessar esta pasta digitando `%APPDATA%\QGISRed` diretamente na barra de endereço do Windows Explorer.

---

## Atualizar dependências

Quando uma nova versão do QGISRed é lançada que inclui uma versão atualizada das dependências, o plugin detecta isso automaticamente na inicialização e propõe a atualização com a mesma caixa de diálogo de confirmação.

---

## Solução de problemas

**O download falha ou é interrompido**

Verifique se você possui uma conexão com a Internet e se nenhum firewall corporativo está bloqueando o download. Se o problema persistir, entre em contato com o administrador da rede para permitir conexões de saída do QGIS.

**O plugin exibe a caixa de diálogo de dependências sempre que é aberto**

Isso significa que as bibliotecas não foram instaladas corretamente nas sessões anteriores. Verifique se a pasta `%APPDATA%\QGISRed\` existe e contém os arquivos `.dll`. Se estiver vazio, exclua-o completamente e tente a instalação novamente.

**O dispositivo não tem acesso à internet**

Você pode instalar dependências offline se tiver os arquivos necessários:

1. **ZIP de dependências**: solicita a alguém com o plugin já instalado o conteúdo de sua pasta `%APPDATA%\QGISRed\` (mesma versão do QGISRed). Copie esses arquivos para sua própria pasta `%APPDATA%\QGISRed\`.
2. **Instalador do .NET Framework 4.8.1**: Baixe para outro computador com internet ou solicite o MSI a alguém. Execute-o antes de usar o plugin.

Depois que as DLLs forem copiadas e com o .NET Framework 4.8.1 instalado, o plugin funcionará sem a necessidade de conexão com a Internet em nenhum momento.
