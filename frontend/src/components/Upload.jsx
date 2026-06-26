import axios from "axios";
import {useState} from "react";


function Upload(){

const [status,setStatus]=useState("");


const uploadPDF = async(e)=>{


const file=e.target.files[0];


const formData=new FormData();

formData.append("file",file);


setStatus("Uploading PDF...");


const response=await axios.post(

`${import.meta.env.VITE_BACKEND_URL}/upload`,

formData

);


console.log(response.data);


setStatus("✅ PDF Ready for questions");


}



return(

<div>


<h2>
📄 Upload PDF
</h2>


<input

type="file"

onChange={uploadPDF}

/>


<p>{status}</p>


</div>


)


}


export default Upload;