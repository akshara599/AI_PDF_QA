import {useState} from "react";

import axios from "axios";


function Chat(){


const [question,setQuestion]=useState("");

const [answer,setAnswer]=useState("");



const askQuestion=async()=>{


const response = await axios.post(

"http://127.0.0.1:8000/chat",

null,

{
params:{
question:question
}
}

);


setAnswer(
response.data.answer
);


}



return(

<div>


<h2>
Ask Question
</h2>


<input

value={question}

onChange={(e)=>
setQuestion(e.target.value)
}

/>


<button onClick={askQuestion}>

Ask

</button>


<h3>
Answer:
</h3>


<p>

{answer}

</p>


</div>


)

}


export default Chat;