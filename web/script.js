function enviarImagem() {
    const url = 'http://127.0.0.1:5000';
    const inputFile = document.getElementById('input-file');
    const file = inputFile.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('image', file);

        fetch(url, {
            method: 'POST',
            body: formData
        })
            .then(response => response.text())
            .then(data => {
                console.log(data);
            })
            .catch(error => {
                console.error('Erro:', error);
            });
    }
}
