<template>
    <div>
        <h3>Lista Tasks</h3>

        <table class="striped">
            <thead>
                <tr>
                    <th width="10%">Título</th>
                    <th width="40%">Descrição</th>
                    <th>Status</th>
                    <th>Data de Criação</th>
                    <th>Última Edição</th>
                    <th>Data de Conclusão</th>
                    <th>
                        <select type="text" class="browser-default" v-model="filtroConcluida">
                            <option :value="null">Sem Filtro</option>
                            <option :value="1">Apenas Concluidas</option>
                            <option :value="0">Apenas Não Concluidas</option>
                        </select>
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="task in this.tasks" :key="task.id" v-if="filtroConcluida == null || task.status == filtroConcluida">              
                        <td v-if="editandoTask === task.id">
                            <input id="titulo" type="text" class="validate" v-model="task.titulo">
                        </td>
                        <td v-else>{{task.titulo}}</td>
                        <td v-if="editandoTask === task.id">
                            <input id="titulo" type="text" class="validate" v-model="task.descricao">
                        </td>
                        <td v-else>{{task.descricao}}</td>
                        <td>
                            <label>
                                <input v-on:change="alterarStatusTask(task)"  type="checkbox" checked="checked" v-model="task.status"/>
                                <span></span>
                            </label>
                        </td>

                        <td>{{task.created}}</td>
                        <td>{{task.edited}}</td>
                        <td>{{task.concluded}}</td>
                        <td v-if="editandoTask === task.id">
                            <button v-on:click="atualizarTask(task)" class="btn-floating waves-effect waves-light green"><i  class="material-icons"> save </i> </button>
                        </td>
                        <td v-else>
                            <button v-on:click="editandoTask = task.id" class="btn-floating waves-effect waves-light blue"><i  class="material-icons"> edit </i> </button>
                            <button v-on:click="excluirTask(task)" class="btn-floating waves-effect waves-light red"><i  class="material-icons">delete</i></button>
                        </td>
                </tr>
            </tbody> 
        </table>
        <div class="novaTask">
            <b> Criar Nova Task </b>
        </div>
        <div class="row">
            <div class="input-field col s3">
                <input id="titulo" placeholder="Título" type="text" class="validate" v-model="novaTask.titulo">
            </div>
            <div class="input-field col s6">
                <input id="descricao" placeholder="Descrição" type="text" class="validate" v-model="novaTask.descricao">
            </div>
            <div class="input-field col s3">
                <a v-on:click="criarTask()" class="waves-effect waves-light btn">Save</a>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            filtroConcluida: null,
            editandoTask: null,
            tasks: null,
            novaTask: {
                titulo: "",
                descricao: ""
            }
        }
    },
    mounted(){
        fetch('http://localhost:8000/api/task/', {
        })
        .then(response => response.json())
        .then((data) => {
            this.tasks = data;
        })
    },
    methods: {
        alterarStatusTask(task){
            fetch('http://localhost:8000/api/task/' + task.id + '/', {
                method: "POST"
            })
            .then(request => request.json())
            .then((data) => {
                task.concluded = data["concluded"]
            })
        },
        excluirTask(task){
            fetch('http://localhost:8000/api/task/' + task.id + '/', {
                method: "DELETE"
            })
            .then(() => {
                var index = this.tasks.indexOf(task);
                this.tasks.splice(index, 1);
            })
        },
         criarTask() {
            fetch("http://localhost:8000/api/task/", {
                body: JSON.stringify(this.novaTask),
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
            })
            .then(request => request.json())
            .then((data) => {
                this.tasks.push(data);
                this.novaTask.titulo = null;
                this.novaTask.descricao = null;
            })
        },
        atualizarTask(task){
            fetch('http://localhost:8000/api/task/' + task.id + '/', {
                body: JSON.stringify(task),
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
            })
            .then(request => request.json())
            .then((data) => {
                task.edited = data.edited;
                this.editandoTask = null;
            })
        }
    }
}
</script>

<style>
@import "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/css/materialize.min.css";
@import "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/js/materialize.min.js";
@import "https://fonts.googleapis.com/icon?family=Material+Icons";
@import "https://fonts.google.com/specimen/Oxygen";

h3 {
    padding-bottom: 30px;
    margin-left: 2%;
    font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif
}

.novaTask {
    margin-top: 30px;
    margin-left: 0.5%;
    font-size: 18px;
}

table th {
    padding-top: 12px;
    padding-bottom: 12px;
    text-align: left;
    background-color: #A0A0A0;
    color: white;
    border-bottom: 5mm;
    border-color: gray;
    font-size: 18px
}

table td, table th {
    border: 1px solid #ddd;
    padding: 8px;
}

</style>