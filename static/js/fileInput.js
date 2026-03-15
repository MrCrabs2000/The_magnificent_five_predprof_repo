let fileInputs = document.querySelectorAll(".file-input");

fileInputs.forEach(fileInput => {
    let input = fileInput.querySelector("input[type='file']");
    let textContainer = fileInput.querySelector(".file-input__file");

    input.addEventListener('change', function() {
        let file = this.files[0];
        textContainer.value = file.name;
    });
});
