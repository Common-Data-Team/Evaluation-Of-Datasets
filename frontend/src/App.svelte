<script>

</script>

<main>
    <header>
        <img src="logo.svg" alt="cd">
        <p>Check the Data</p>
    </header>
    <p class="tagline">Узнайте особенности вашего датасета при помощи наших алгоритмов!</p>
    <form>
        <div class="input-zone"
             on:dragover={(e) => {document.getElementById('file-label').style.filter="blur(1px)"}}
             on:dragleave={(e) => {document.getElementById('file-label').style.filter="blur(0)"}}
        >
        <input type="file" id="file">
            <label for="file" id="file-label">Выберите файл для загрузки или перетащите сюда</label>
        </div>
    </form>
</main>
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Raleway:wght@800&family=Roboto&display=swap" rel="stylesheet">
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

    .tagline {
        font-family: 'Roboto', sans-serif;
        font-size: max(25px, 1.8vw);
        text-align: center;
        margin: 50px;
    }

    .input-zone {
        background-color: #F9F9F9;
        border: 2px #282828 dashed;
        width: 80%;
        height: 400px;
        margin: 10px auto;
    }

    form input {
        display: none;
    }
</style>