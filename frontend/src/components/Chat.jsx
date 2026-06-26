import {useState} from "react";
import axios from "axios";


function Chat(){

    const [question,setQuestion] = useState("");
    const [answer,setAnswer] = useState("");


    const askQuestion = async()=>{


        const response = await axios.post(

            `${import.meta.env.VITE_BACKEND_URL}/chat`,

            {
                question: question
            }

        );


        setAnswer(response.data.answer);

    }


    return (

        <div>


            <h2>
                Ask PDF
            </h2>


            <input

                value={question}

                onChange={(e)=>setQuestion(e.target.value)}

                placeholder="Ask something..."

            />


            <button onClick={askQuestion}>
                Ask
            </button>


            <h3>
                {answer}
            </h3>


        </div>

    )

}


export default Chat;