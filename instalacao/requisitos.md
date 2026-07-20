# Requisitos do sistema

Antes de instalar o QGISRed, verifique se o seu computador atende aos seguintes requisitos.

---

## Sistema operacional

**Windows 10 ou superior (x64)**.

QGISRed não está disponível para Linux ou macOS. O mecanismo de cálculo utiliza DLLs compiladas em .NET que requerem o ambiente Windows.

---

##QGIS

**Versão 3.28 ou superior**, incluindo a série 4.x.

### Como verificar sua versão do QGIS

Vá para **Ajuda → Sobre o QGIS**. A versão aparece na primeira linha do diálogo.

Se a sua versão for anterior à 3.28, baixe a versão LTR (Long Term Release) mais recente em [qgis.org](https://qgis.org/download/).

> Versões anteriores a 3.28 não são mais suportadas pelo plugin desde QGISRed 0.18. Se você precisar trabalhar com uma versão mais antiga do QGIS, use QGISRed 0.17 ou anterior.

---

##.NET Framework

**Versão 4.8.1**.

### Como verificar se está instalado

1. Abra **Painel de Controle → Programas → Programas e Recursos**.
2. Clique em **Ativar ou desativar recursos do Windows**.
3. Procure **.NET Framework 4.8.1** na lista. Se aparecer marcado, já está instalado.

No Windows 11 e em versões recentes do Windows 10, o .NET Framework 4.8.1 pode vir pré-instalado. Em versões mais antigas ou no Windows Server, pode ser necessário baixá-lo e instalá-lo manualmente da Microsoft.

---

## Conexão com a Internet

Necessário **na primeira vez** que o plugin é utilizado, para baixar as dependências (as DLLs do mecanismo de cálculo). Downloads subsequentes (atualizações de plugins) também requerem conexão.

Depois que as dependências forem instaladas, o QGISRed pode funcionar **sem conexão com a internet**.

> Se você não tiver uma conexão com a internet, você pode instalar as dependências manualmente: peça a alguém para lhe fornecer o ZIP das dependências e o instalador MSI do .NET Framework 4.8.1. Com ambos os arquivos você poderá completar a instalação sem precisar de conexão. Veja a seção [Gerenciamento de dependências](dependencias.md) para mais detalhes.
