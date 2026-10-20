// Fixed texts of the manual's own chrome (header, buttons, search...) -- the
// chapters' text lives in the repo's own *.md files. One object per language
// in this single file (same content on the 4 branches) so a build only needs
// to pick UI[lang], not maintain 4 separate files.

export type ManualLanguage = "es" | "en" | "fr" | "pt-BR";

export interface ManualUi {
  htmlLang: string;
  manualTitle: string;
  manualSubtitle: string;
  searchPlaceholder: string;
  searchNoResults: string;
  downloadPdf: string;
  printPdf: string;
  menu: string;
  previous: string;
  next: string;
  onThisPage: string;
  contents: string;
  anchorLabel: string;
  callouts: Record<"note" | "warning", string>;
  /** `toLocaleDateString` locale for the PDF cover. */
  dateLocale: string;
  coverBy: string;
}

export const UI: Record<ManualLanguage, ManualUi> = {
  es: {
    htmlLang: "es",
    manualTitle: "Manual de usuario",
    manualSubtitle: "Plugin de QGIS para el modelado y la gestión de redes de distribución de agua",
    searchPlaceholder: "Buscar en el manual...",
    searchNoResults: "Sin resultados",
    downloadPdf: "Descargar PDF",
    printPdf: "Imprimir / guardar como PDF",
    menu: "Menú",
    previous: "Anterior",
    next: "Siguiente",
    onThisPage: "En esta página",
    contents: "Contenido",
    anchorLabel: "Enlace a esta sección",
    callouts: { note: "Nota", warning: "Atención" },
    dateLocale: "es-ES",
    coverBy: "Grupo de Redes Hidráulicas REDHISP · Universitat Politècnica de València",
  },
  en: {
    htmlLang: "en",
    manualTitle: "User manual",
    manualSubtitle: "QGIS plugin for modelling and managing water distribution networks",
    searchPlaceholder: "Search the manual...",
    searchNoResults: "No results",
    downloadPdf: "Download PDF",
    printPdf: "Print / save as PDF",
    menu: "Menu",
    previous: "Previous",
    next: "Next",
    onThisPage: "On this page",
    contents: "Contents",
    anchorLabel: "Link to this section",
    callouts: { note: "Note", warning: "Warning" },
    dateLocale: "en-GB",
    coverBy: "REDHISP Hydraulic Networks Group · Universitat Politècnica de València",
  },
  fr: {
    htmlLang: "fr",
    manualTitle: "Manuel d'utilisation",
    manualSubtitle:
      "Extension QGIS pour la modélisation et la gestion des réseaux de distribution d'eau",
    searchPlaceholder: "Rechercher dans le manuel...",
    searchNoResults: "Aucun résultat",
    downloadPdf: "Télécharger le PDF",
    printPdf: "Imprimer / enregistrer en PDF",
    menu: "Menu",
    previous: "Précédent",
    next: "Suivant",
    onThisPage: "Sur cette page",
    contents: "Sommaire",
    anchorLabel: "Lien vers cette section",
    callouts: { note: "Remarque", warning: "Attention" },
    dateLocale: "fr-FR",
    coverBy: "Groupe de Réseaux Hydrauliques REDHISP · Universitat Politècnica de València",
  },
  "pt-BR": {
    htmlLang: "pt-BR",
    manualTitle: "Manual do usuário",
    manualSubtitle: "Plugin do QGIS para modelagem e gestão de redes de distribuição de água",
    searchPlaceholder: "Buscar no manual...",
    searchNoResults: "Nenhum resultado",
    downloadPdf: "Baixar PDF",
    printPdf: "Imprimir / salvar como PDF",
    menu: "Menu",
    previous: "Anterior",
    next: "Próximo",
    onThisPage: "Nesta página",
    contents: "Conteúdo",
    anchorLabel: "Link para esta seção",
    callouts: { note: "Nota", warning: "Atenção" },
    dateLocale: "pt-BR",
    coverBy: "Grupo de Redes Hidráulicas REDHISP · Universitat Politècnica de València",
  },
};
