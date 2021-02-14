<script>
    import Statistics from './_components/Statistics.svelte'
    import { SpinLine } from 'svelte-loading-spinners'

    let show_statistics = false;
    let files = [];
    const url = 'https://backendatasets.commondata.ru/'
    async function sendFile() {
        if (files.length === 0) {
            let label_text = document.getElementById('input-label')
            label_text.innerText = 'Вы не выбрали файл!';
            label_text.style.color="#FF0033";
        }
        if (files[0].name.split('.').pop() == 'csv') {
            let headers = new Headers();
            let form_data = new FormData();
            form_data.append("file", files[0], files[0].name);
            let response;
            show_statistics = true;
            document.getElementById('statistics-block').scrollIntoView({block: 'start', behavior: 'smooth'});
            try {
                response = await fetch(url + 'upload', {
                    method: "POST",
                    body: form_data
                }).then(response => response.json())
            } catch (error) {
                throw new Error(error.text)
            }
            return response;
        }
    }

    let promise;

    function handleClick() {
        promise = sendFile();
    }

    function overrideDefault(event) {
        event.preventDefault();
        event.stopPropagation();
    }

    function addFile(event) {
        files = event.dataTransfer.files;
        console.log(files[0].name);
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
<header>
    <a href="/"><img src="logo.svg" alt="cd"></a>
    <a href="/" class="main-link"><p>Check the Data</p></a>
</header>
<main>
    <div class="first-view">
        <p class="tagline">Узнайте, как улучшить свой датасет с помощью наших алгоритмов</p>
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
        <button id="submit-button" on:click={handleClick}>Обработать</button>
    </div>
    <div id="statistics-block">
    {#if show_statistics}
        {#await promise}
            <div class="spinner">
            <SpinLine size="100" color="#282828" duration="4s"/>
            </div>
        {:then data}
            <h1>Результаты анализа</h1>
            <Statistics {data}/>
        {/await}
    {/if}
    </div>
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
        font-weight: 800;
        font-size: 50px;
        margin: 0 0 0 20px;
    }

    main {
        text-align: center;
    }

    .first-view {
        height: 90vh;
    }

    .tagline {
        font-family: 'Roboto', sans-serif;
        font-size: max(20px, 1.5vw);
        text-align: center;
        margin: 20px 50px 50px 50px;
    }

    .input-zone {
        background-color: #FEFEFE;
        border: 2px #282828 dashed;
        width: 70%;
        height: 350px;
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

    #statistics-block {
        padding: 50px 0 0 0;
        height: 800px;
    }

    #statistics-block h1 {
        font-family: Raleway;
        margin: 0;
    }

    .spinner {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 100px auto;
    }

    .main-link {
        text-decoration: none;
        color: #282828;
    }
</style>