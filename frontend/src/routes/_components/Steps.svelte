<div class="component">
    <h1 class="title">Этапы</h1>
    <div class="step-block">
        <h1 class="step-number">01</h1>
        <div class="step-info">
            <h1>Соберите датасет</h1>
            <p>Найдите готовый датасет в интернете или воспользуйтесь нашей платформой донорства данных Common Data</p>
        </div>
        <img src="images/world.svg" alt="">
    </div>
    <div class="step-block right">
        <img src="images/recomendations.svg" alt="">
        <h1 class="step-number">02</h1>
        <div class="step-info">
            <h1>Получите рекомендации</h1>
            <p>Загрузите датасет на нашу платформу и получите практические советы о том, как улучшить ваш датасет</p>
        </div>
    </div>
    <div class="step-block">
        <h1 class="step-number">03</h1>
        <div class="step-info">
            <h1>Обработайте датасет</h1>
            <p>Воспользуйтесь нашими инструкциями или автоматизированным алгоритмом для обработки и разметки датасета</p>
        </div>
        <img src="images/dataset.svg" alt="">
    </div>
</div>

<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@700&display=swap" rel="stylesheet">
<style>
    .component {
        max-width: 1000px;
        margin: auto;
    }

    .title {
        text-align: center;
    }

    .step-block {
        display: flex;
        width: 100%;
        margin: 80px 20px;
    }

    .right {
        justify-content: flex-end;
    }

    .step-block h1 {
        margin: 0;
        font-size: calc(24px + (36 - 24) * ((100vw - 300px) / (1440 - 300)));
    }

    .step-number {
        font-family: 'Red Hat Display', sans-serif;
        color: #1355FF;
    }
    .step-info {
        font-family: 'Roboto', sans-serif;
        text-align: left;
        margin: 0 30px;
    }

    .step-info h1 {
        margin-bottom: 0;
    }

    .step-info p {
        width: 400px;
        margin-top: 25px;
        font-size: 15px;
        line-height: 2;
    }

    .step-block img {
        width: 200px;
        margin-right: 50px;
    }

    @media (max-width: 700px) {

        .step-block img {
            display: none;
        }

        .step-info p {
            width: 200px;
        }
    }

</style>