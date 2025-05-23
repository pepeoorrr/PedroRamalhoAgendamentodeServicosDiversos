TextDecoderStream// Função para carregar agendamentos salvos
function carregarAgendamentos() {
    const tabela = document.querySelector("#tabelaAgendamentos tbody");
    tabela.innerHTML = "";

    const agendamentos = JSON.parse(localStorage.getItem("agendamentos")) || [];

    agendamentos.forEach((agendamento, index) => {
        const linha = document.createElement("tr");

        linha.innerHTML = `
            <td>${agendamento.nome}</td>
            <td>${agendamento.servico}</td>
            <td>${agendamento.data}</td>
            <td>${agendamento.endereco}</td>
            <td><button class="btn-excluir" data-index="${index}">Excluir</button></td>
        `;

        tabela.appendChild(linha);
    });
}

// Função para salvar agendamento no localStorage
function salvarAgendamento(event) {
    event.preventDefault();

    const nome = document.getElementById("nome").value.trim();
    const servico = document.getElementById("servico").value.trim();
    const data = document.getElementById("data").value;
    const endereco = document.getElementById("endereco").value.trim();

    if (!nome || !servico || !data) {
        alert("Preencha todos os campos obrigatórios.");
        return;
    }

    const novoAgendamento = { nome, servico, data, endereco };

    const agendamentos = JSON.parse(localStorage.getItem("agendamentos")) || [];
    agendamentos.push(novoAgendamento);
    localStorage.setItem("agendamentos", JSON.stringify(agendamentos));

    document.getElementById("formAgendamento").reset();
    carregarAgendamentos();
}

// Função para excluir agendamento
function excluirAgendamento(index) {
    const confirmar = confirm("Deseja realmente excluir este agendamento?");
    if (!confirmar) return;

    const agendamentos = JSON.parse(localStorage.getItem("agendamentos")) || [];
    agendamentos.splice(index, 1);
    localStorage.setItem("agendamentos", JSON.stringify(agendamentos));
    carregarAgendamentos();
}

// Adiciona eventos
document.addEventListener("DOMContentLoaded", () => {
    carregarAgendamentos();

    document.getElementById("formAgendamento").addEventListener("submit", salvarAgendamento);

    document.querySelector("#tabelaAgendamentos tbody").addEventListener("click", (event) => {
        if (event.target.classList.contains("btn-excluir")) {
            const index = event.target.getAttribute("data-index");
            excluirAgendamento(index);
        }
    });
});
