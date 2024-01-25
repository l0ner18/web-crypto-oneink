import React, { useState } from "react";

const Sdes_alghoritm = () => {

    const [key, setKey] = useState(null);
    const [message, setMessage] = useState(null);
    const [result, setResult] = useState(null)

    const handleClick = () => {
        const data = { key, message }

        fetch('/alghoritm-sdes', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
            .then(response => response.json())
            .then(result => {
                console.log(result.result)
                setResult(result.result)
            })
            .catch(error => {
                console.log("no")
                console.error('Ошибка:', error);
            });
    }

    return (
        <div className="App" style={{ "marginTop": "80px" }}>
            <h1>S-DES</h1>
            <h1>Ключ</h1>
            <input onChange={(event) => setKey(event.target.value)} />

            <h1>Сообщение</h1>
            <input onChange={(event) => setMessage(event.target.value)} /><br></br>

            <button onClick={handleClick}>Ввод</button>

            <h3>Результат: {result}</h3>
        </div>
    )
}

export default Sdes_alghoritm;