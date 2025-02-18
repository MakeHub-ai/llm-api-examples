import dotenv from 'dotenv';

dotenv.config();

async function main() {
    try {
        const API_KEY = process.env.MAKEHUB_API_KEY;
        
        const response = await fetch(
            'https://api.makehub.ai/v1/chat/completions?min_throughput=150&max_latency=1000',
            {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${API_KEY}`,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    messages: [{ role: 'user', content: 'Hello, world!' }],
                    model: 'meta/Llama-3.3-70B-Instruct-fp16'
                })
            }
        );

        const completion = await response.json();
        console.log(completion.choices[0].message.content);
    } catch (error) {
        console.error('Error:', error);
    }
}

main();
