import {useState} from "react";
import axios from "axios";


function Chat(){


const [question,setQuestion]=useState("");

const [answer,setAnswer]=useState("");

const [loading,setLoading]=useState(false);



const askQuestion=async()=>{


setLoading(true);


const response=await axios.post(

`${import.meta.env.VITE_BACKEND_URL}/chat`,

{
question
}

);


setAnswer(response.data.answer);


setLoading(false);


}



return(

<div>


<h2>
💬 Ask PDF
</h2>


<div className="chatBox">


<input

placeholder="Ask something..."

value={question}

onChange={(e)=>setQuestion(e.target.value)}

/>


<button onClick={askQuestion}>
Ask
</button>


</div>


{

loading ?

<p>
Thinking...
</p>

:

<div className="answer">

{answer}

</div>

}



</div>

)


}


export default Chat;