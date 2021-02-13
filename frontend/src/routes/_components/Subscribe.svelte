<form class="wrapper_inpt">
    <input type="email" placeholder="help@commondata.ru">
    <input type="submit" class="btn_area" value="Subscribe">
</form>

<style>
    * {
        margin: 0;
        padding: 0;
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        box-sizing: border-box;
        font-family: sans-serif;
        outline: none;
    }

    .wrapper_inpt {
        width: 400px;
        height: 50px;
        border-radius: 20px;
        border: 1px solid #fff;
        background-color: #fff;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0px 8px 80px rgba(0, 0, 0, 0.06);
        padding: 5px;
    }

    .btn_area {
        width: 100px;
        height: 40px;
        background: #1355FF;
        border-radius: 20px;
        color: #fff;
        display: flex;
        align-items: center;
        text-align: center;
        cursor: pointer;
    }

    input {
      border: none;
      background: none;
      width: calc(100% - 84px);
      height: 100%;
      text-indent: 12px;
    }
</style>