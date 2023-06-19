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
          fazerDownloadArquivo(data);
        })
        .catch(error => console.log(error));
    }
}

function fazerDownloadArquivo(response) {
    const nomeArquivo = 'arquivo.txt';
    const blob = new Blob([response], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
  
    const linkDownload = document.createElement('a');
    linkDownload.href = url;
    linkDownload.download = nomeArquivo;
    linkDownload.click();
  
    URL.revokeObjectURL(url);
  }