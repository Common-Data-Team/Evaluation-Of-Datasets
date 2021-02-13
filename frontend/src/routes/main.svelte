<script>
import Steps from './_components/Steps.svelte';
import {push} from 'svelte-spa-router';
import Subscribe from './_components/Subscribe.svelte';
import Footer from './_components/Footer.svelte';
</script>
<header>
    <img id="logo" src="logo.svg" alt="cd">
    <div class="social-icons">
        <a href="https://github.com/Common-Data-Team"><img src="./images/icons/Github_black.svg" alt="github-logo-icon"></a>
        <a href="https://www.patreon.com/commondatateam"><img src="./images/icons/Patreon_black.svg" alt="patreon-logo-icon"></a>
        <a href="https://www.linkedin.com/company/common-data-team"><img src="./images/icons/linkedIN_black.svg" alt="linkedin-logo-icon"></a>
        <a href="https://t.me/commondatateam"><img src="./images/icons/Telegram_black.svg" alt="telegram-logo-icon"></a>
    </div>
</header>
<main>
    <div class="first-view">
        <div class="first-block">
            <div class="description">
                <h1>Check the Data</h1>
                <p>Сервис для аналитики и улучшения датасетов</p>
                <button on:click={() => push('/service')}>Попробовать</button>
            </div>
            <div class="image">
                <img src="./images/main_img.svg" alt="main-image">
            </div>
        </div>
    </div>
    <div class="second-block">
        <h1>Для кого?</h1>
        <div class="cards">
            <div class="card">
                <img src="./images/developer.svg" alt="developer-image">
                <h3>Разработчики</h3>
                <p>Профессионалы могут  удостовериться в качестве данных и ускорить процесс обработки датасета</p>
            </div>
            <div class="card">
                <img src="./images/new.svg" alt="new-analytics-image">
                <h3>Начинающие аналитики</h3>
                <p>Начинающие аналитики могут научиться обработке датасетов с помощью наших инструкций</p>
            </div>
            <div class="card">
                <img src="./images/not_it.svg" alt="not-it-image">
                <h3>Не ИТ специалисты</h3>
                <p>Те, кто принимают решения на основе данных, могут воспользоваться автоматизированным алгоритмом и обработать датасет в один клик</p>
            </div>
        </div>
    </div>
    <Steps/>
    <h1 class="subscribe">Подписаться на новости сервиса</h1>
    <div class="subscribe">
        <Subscribe></Subscribe>
    </div>
    <Footer></Footer>
</main>
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;800&family=Roboto&display=swap" rel="stylesheet">
<style>
    button:hover {
        cursor: pointer;
    }

    main {
        width: 100%;
        height: 100%;
    }
    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 30px;
    }

    .second-block h1 {
        text-align: center;
        margin: 100px 0 50px 0;
    }

    .cards {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .card {
        background: #FFFFFF;
        width: 20%;
        margin: 2%;
        padding: 20px;
        height: auto;
        box-shadow: 6px 11px 19px rgba(193, 193, 193, 0.37), -21px -33px 86px #FFFFFF;
        border-radius: 10px;
    }

    .description {
        text-align: left;
    }

    .first-view {
        width: 100%;
        height: 90vh;
    }

    .first-block {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .subscribe {
        display: flex;
        justify-content: center;
        text-align: center;
    }

    header img {
        height: 60px;
    }

    .social-icons img {
        height: 36px;
        padding: 2px;
    }

    .image img {
        max-width: 600px;
    }

    .description button {
        background-color: #282828;
        font-family: 'Raleway', sans-serif;
        font-weight: 400;
        color: #FFFFFF;
        border-radius: 8px;
        padding: 15px 45px;
        margin: 20px auto;
    }


</style>