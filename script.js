const apiUrl = 'http://127.0.0.1:5000'; 

function listarTarefas() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const tarefasDiv = document.getElementById('tarefas');
            tarefasDiv.innerHTML = ''; 

            data.forEach(tarefa => {
                const tarefaDiv = document.createElement('div');
                tarefaDiv.classList.add('tarefa', tarefa.stat === 'completa' ? 'completed' : 'pending');
                tarefaDiv.innerHTML = `
                    <p><strong>Tarefa:</strong> ${tarefa.nome_tarefa}</p>
                    <p><strong>Status:</strong> ${tarefa.stat}</p>
                    <button onclick="marcarComoCompleta(${tarefa.id})">Marcar como Completa</button>
                    <button onclick="marcarComoPendente(${tarefa.id})">Marcar como Pendente</button>
                    <button onclick="deletarTarefa(${tarefa.id})">Remover</button>
                `;
                tarefasDiv.appendChild(tarefaDiv);
            });
        })
        .catch(error => console.error('Erro ao listar tarefas:', error));
}

document.getElementById('form-nova-tarefa').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const nomeTarefa = document.getElementById('nome-tarefa').value;

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nome: nomeTarefa }) 
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        listarTarefas(); 
    })
    .catch(error => console.error('Erro ao adicionar tarefa:', error));
});

function marcarComoCompleta(id) {
    fetch(`${apiUrl}/completa/${id}`, {
        method: 'PUT'
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        listarTarefas(); 
    })
    .catch(error => console.error('Erro ao marcar como completa:', error));
}

function marcarComoPendente(id) {
    fetch(`${apiUrl}/pendente/${id}`, {
        method: 'PUT'
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        listarTarefas(); 
    })
    .catch(error => console.error('Erro ao marcar como pendente:', error));
}

function deletarTarefa(id) {
    fetch(`${apiUrl}/remover/${id}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        listarTarefas(); 
    })
    .catch(error => console.error('Erro ao remover tarefa:', error));
}

listarTarefas();