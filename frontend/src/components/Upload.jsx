import axios from "axios";


function Upload(){

    const uploadPDF = async(e)=>{


        const file = e.target.files[0];


        const formData = new FormData();


        formData.append(
            "file",
            file
        );


        const response = await axios.post(

            "http://127.0.0.1:8000/upload",

            formData

        );


        console.log(response.data);

    }



    return (

        <div>

            <h2>
                Upload PDF
            </h2>


            <input

                type="file"

                onChange={uploadPDF}

            />

        </div>

    )

}


export default Upload;