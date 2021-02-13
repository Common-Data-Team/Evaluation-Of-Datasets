<script>
    let file;

    function overrideDefault(event) {
        event.preventDefault();
        event.stopPropagation();
    }

    function addFile(event) {
        file = event.dataTransfer.files;
    }
</script>
<header>
    <img src="logo.svg" alt="cd">
    <p>Check the Data</p>
</header>
<main>
    <p class="tagline">Узнайте особенности вашего датасета при помощи наших алгоритмов!</p>
    <div class="input-zone">
    <input type="file" id="file" name="files" bind:files={file}>
        <label for="file" id="file-label"
        on:dragover={overrideDefault}
        on:dragenter={overrideDefault}
        on:dragleave={overrideDefault}
        on:drop={(e) => {overrideDefault(e); addFile(e);}}
        >
            <img src="download.svg" alt="">
            <p>Выберите файл для загрузки или перетащите сюда</p>
        </label>
    </div>
<button class="submit-button" >Обработать</button>
</main>
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;800&family=Roboto&display=swap" rel="stylesheet">
<style>
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
        font-size: max(25px, 1.8vw);
        text-align: center;
        margin: 20px 50px 50px 50px;
    }

    .input-zone {
        background-color: #F9F9F9;
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
    }

    .submit-button {
        background-color: #282828;
        font-family: 'Raleway', sans-serif;
        font-weight: 400;
        color: #FFFFFF;
        border-radius: 8px;
        padding: 20px 45px;
        margin: 20px auto;
    }
    .submit-button:hover {
        cursor: pointer;
    }
</style>