<script>
    let files;

    function overrideDefault(event) {
        event.preventDefault();
        event.stopPropagation();
    }

    function addFile(event) {
        files = event.dataTransfer.files;
        changeLabel();
    }

    function changeLabel() {
        let label_text = document.getElementById('input-label');
        if (files) {
            if (files[0].name.split('.').pop() != 'csv') {
                label_text.innerText = files[0].name + ' - формат не поддерживается!';
                label_text.style.color="#FF0033";

            } else {
                label_text.innerText = files[0].name + ' - загружен';
                label_text.style.color="#313131";
            }
        } else {
            label_text.innerText = 'Ошибка при загрузке файла!';
            label_text.style.color="#FF0033";
        }
    }
</script>
<div id="window">
<header>
    <img src="logo.svg" alt="cd">
    <p>Check the Data</p>
</header>
<main>
    <p class="tagline">Узнайте особенности вашего датасета при помощи наших алгоритмов!</p>
    <div class="input-zone">
    <input type="file" id="file" name="files" bind:files on:change={changeLabel}>
        <label for="file" id="file-label"
        on:dragover={(e) => {overrideDefault(e); document.getElementById('file-label').style.filter="blur(1px)"}}
        on:dragenter={overrideDefault}
        on:dragleave={(e) => {overrideDefault(e); document.getElementById('file-label').style.filter="blur(0)"}}
        on:drop={(e) => {overrideDefault(e); addFile(e); document.getElementById('file-label').style.filter="blur(0)"}}
        >
            <img src="download.svg" alt="">
            <p id="input-label">Выберите файл для загрузки или перетащите сюда</p>
        </label>
    </div>
<button id="submit-button">Обработать</button>
</main>
</div>
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;800&family=Roboto&display=swap" rel="stylesheet">
<style>
    #window {
        background-color: #E5E5E5;
    }

    header {
        display: flex;
        align-items: center;
        padding: 30px;
    }

    header img {
        height: 60px;
    }

    header p {
        font-family: 'Raleway', sans-serif;
        font-size: 40px;
        margin: 0 0 0 20px;
    }

    main {
        text-align: center;
    }

    .tagline {
        font-family: 'Roboto', sans-serif;
        font-size: max(20px, 2vw);
        text-align: center;
        margin: 20px 50px 50px 50px;
    }

    .input-zone {
        background-color: #FEFEFE;
        border: 2px #282828 dashed;
        width: 80%;
        height: 400px;
        margin: 10px auto;
    }

    input {
        display: none;
    }

    label {
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

    label:hover {
        cursor: pointer;
    }

    label p {
        font-family: 'Raleway', sans-serif;
        font-weight: 400;
        font-size: 20px;
        color: #313131;
    }

    #submit-button {
        background-color: #282828;
        font-family: 'Raleway', sans-serif;
        font-weight: 400;
        color: #FFFFFF;
        border-radius: 8px;
        padding: 20px 45px;
        margin: 20px auto;
    }
    #submit-button:hover {
        cursor: pointer;
    }
</style>