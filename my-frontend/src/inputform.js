// src/InputForm.js
import React, { useState } from 'react';
import axios from 'axios';

const InputForm = () => {
    const [data, setData] = useState('');
    const [file, setFile] = useState(null);
    const [response, setResponse] = useState(null);
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setResponse(null);

        try {
            const base64File = file ? await convertFileToBase64(file) : '';
            const jsonData = JSON.parse(data);

            const result = await axios.post('http://127.0.0.1:5000/bfhl', {
                data: jsonData.data,
                file_b64: base64File
            });

            setResponse(result.data);
        } catch (err) {
            setError('Invalid input or API error.');
        }
    };

    const convertFileToBase64 = (file) => {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onloadend = () => resolve(reader.result.split(',')[1]);
            reader.onerror = reject;
            reader.readAsDataURL(file);
        });
    };

    return (
        <div>
            <h2>Submit Data</h2>
            <form onSubmit={handleSubmit}>
                <textarea
                    value={data}
                    onChange={(e) => setData(e.target.value)}
                    placeholder='Enter JSON data here...'
                />
                <input
                    type='file'
                    onChange={(e) => setFile(e.target.files[0])}
                />
                <button type='submit'>Submit</button>
            </form>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {response && (
                <div>
                    <h3>Response:</h3>
                    <pre>{JSON.stringify(response, null, 2)}</pre>
                </div>
            )}
        </div>
    );
};

export default InputForm;
