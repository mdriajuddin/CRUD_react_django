import React, { Component } from 'react';
import axios from 'axios';
const DATA_API = "http://127.0.0.1:8000/api/?format=json"

class App extends Component{
	state ={
		datas:[]
		}

componentDidMount(){
	this.getData()
	}

getData(){
	axios.get(DATA_API).then(res => {
		this.setState({datas: res.data})
		})
	.catch(err =>{
	console.log(err)
	})
     }

render(){
	return(
	<div>
                {this.state.datas.map(item =>(
                <div>
                                           
                        <h1>{item.name}</h1>
                        <h1>{item.job}</h1>
                </div>
                ))}
	</div>
)
}

}
export default App;