'use client'
import { create } from 'domain';
import Papa from 'papaparse';
import React, { useEffect, useState } from 'react'

interface props {
	graphType: string | undefined
}

const FileReader = ( {graphType}: props ) => {

	const acceptableCSVFileTypes = ".csv"

	const [columnNames, setColumnNames] = useState<string[] | undefined>([]);

	/* Parameters to send to FastAPI */
	const [columnGroupName, setColumnGroupName] = useState<string>("");
	const [columnValueName, setColumnValueName] = useState<string>("");
	const [title, setTitle] = useState<string>("Title");
	const [summedData, setSummedData] = useState<string>("sum");
	const [selectedFile, setSelectedFile] = useState<File | null>(null);

	const [imgSrc, setImgSrc] = useState<string | undefined>(undefined);

	async function createPlot() {

		if (!selectedFile) {
        console.error("No file selected");
        return;
    }
		
		const queryForm = new FormData()
		queryForm.append("groupName", columnGroupName)
		queryForm.append("columnValue", columnValueName)
		queryForm.append("title", title)
		queryForm.append("summedData", summedData)
    queryForm.append("csvFile", selectedFile)
		

		try {
				
			const res = await fetch(`http://localhost:8000/${graphType}`, { 
				method: 'POST',
				body: queryForm
			});

			// Convert the response to a Blob
			const blob = await res.blob();

			// Create a temporary object URL for the blob
			const url = URL.createObjectURL(blob);	
			// Store it in state to display it
			setImgSrc(url);
			
		}
		catch (e) {
			console.log(e)
		} 

		
	}


console.log(columnNames);
	
const onFileChangeHandler = (event: any) => {
    const file = event.target.files[0];
    setSelectedFile(file);

    Papa.parse(file, {
        complete: (results: any) => {
            setColumnNames(results.data[0]);
        }
    });
};

	const columnNameOptions = columnNames?.map((columnName, index) =>
		<option key={index} value={columnName}>{columnName}</option>
	) 




  return (
    <div>
			<label htmlFor="csvFileSelector">
				Choose File (csv)
			</label>
			<input type="file" id='csvFileSelector' accept={acceptableCSVFileTypes} onChange={onFileChangeHandler}></input>
			<div>
				<h4>Title (optional):</h4>
				<input type="text" onChange={(e) => setTitle(e.target.value)} />
			</div>
			<div>
				<h4>Group names:</h4>
				<select name="" id="" onChange={(e) => setColumnGroupName(e.target.value)}>
					<option value="">Please select a value</option>
					{columnNameOptions}
				</select>	
			</div>
			<div>
				<h4>Values which are supposed to be shown:</h4>
				<select name="" id="" onChange={(e) => setColumnValueName(e.target.value)}>
					<option value="">Please select a value</option>
					{columnNameOptions}
				</select>	
			</div>
			<div>
				<h4>How should the values be summed:</h4>
				<select name="" id="" onChange={(e) => setSummedData(e.target.value)}>
					<option>Please select a value</option>
					<option value="sum">sum</option>
					<option value="avg">avg</option>
				</select>	
			</div>
			<div>
				<button onClick={createPlot}>Create plot</button>
			</div>

			<div>
				<img src={imgSrc} alt="" />
			</div>
		</div>
  )
}

export default FileReader