<template>
    <table>
        <thead>
            <tr>
                <td>Titulo</td>
                <td width="40%">Descrição</td>
                <td>Status</td>
                <td>Data de Criação</td>
                <td>Ultima Edição</td>
                <td>Data de Conclusão</td>
                <td>
                    <select type="text" class="browser-default" v-model="filtroConcluida">
                        <option :value="null">Sem Filtro</option>
                        <option :value="1">Apenas Concluidas</option>
                        <option :value="0">Apenas Não Concluidas</option>
                    </select>
                </td>
            </tr>
        </thead>
        <tbody>
            <tr v-for="task in this.tasks" :key="task.id" v-if="filtroConcluida == null || task.status == filtroConcluida">              
                    <td>{{task.titulo}}</td>
                    <td>{{task.descricao}}</td>
                    <td>
                        <label>
                            <input type="checkbox" checked="checked" v-model="task.status"/>
                            <span></span>
                        </label>
                    </td>

                    <td>{{task.created}}</td>
                    <td>{{task.edited}}</td>
                    <td>{{task.concluded}}</td>
            </tr>
        </tbody>
    </table>
</template>

<script>
export default {
    data() {
        return {
            filtroConcluida: null,
            tasks: null
        }
    },
    mounted(){
        fetch('http://localhost:8000/api/task/', {
        })
        .then(response => response.json())
        .then((data) => {
            this.tasks = data;
        })
    }
}
</script>

<style>
@import "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/css/materialize.css";
@import "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/js/materialize.js";

</style>