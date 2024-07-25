// Ajoute un écouteur d'événement qui s'exécute lorsque le contenu du document est complètement chargé
document.addEventListener('DOMContentLoaded', () => {
    
    // Sélectionne l'élément avec l'ID 'zoneDepot' et le stocke dans la variable zoneDepot
    const zoneDepot = document.getElementById('zoneDepot');
    
    // Sélectionne l'élément avec l'ID 'fileInput' et le stocke dans la variable fileInput
    const fileInput = document.getElementById('fileInput');
    
    // Sélectionne l'élément avec l'ID 'form-bruteforce' et le stocke dans la variable form
    const form = document.getElementById('form-bruteforce');

    // Ajoute un écouteur d'événement pour 'dragover' sur zoneDepot
    zoneDepot.addEventListener('dragover', (event) => {
        // Empêche le comportement par défaut (important pour permettre le dépôt)
        event.preventDefault();
        
        // Ajoute la classe 'hover' à zoneDepot pour indiquer que l'élément est survolé
        zoneDepot.classList.add('hover');
    });

    // Ajoute un écouteur d'événement pour 'dragleave' sur zoneDepot
    zoneDepot.addEventListener('dragleave', () => {
        // Supprime la classe 'hover' de zoneDepot lorsque l'élément n'est plus survolé
        zoneDepot.classList.remove('hover');
    });

    // Ajoute un écouteur d'événement pour 'drop' sur zoneDepot
    zoneDepot.addEventListener('drop', (event) => {
        // Empêche le comportement par défaut (important pour traiter le dépôt de fichiers)
        event.preventDefault();
        
        // Supprime la classe 'hover' de zoneDepot après le dépôt
        zoneDepot.classList.remove('hover');
        
        // Récupère les fichiers déposés
        const files = event.dataTransfer.files;
        
        // Si au moins un fichier a été déposé
        if (files.length > 0) {
            // Assigne les fichiers déposés à l'input file
            fileInput.files = files;
        }

        // Soumet le formulaire
        form.submit();
    });
});

