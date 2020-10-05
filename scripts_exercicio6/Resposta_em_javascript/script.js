document.querySelector('#contadorNotas').addEventListener('submit', calculaNotas)


class Contador_notas{
    constructor(valor){
        this.valor = valor
        if(this.valor % 5 != 0 || this.valor <= 0){
            throw "Valor inválido! Favor escolher um valor divisível por 5."
        } 
    }

    possibilidade_1(){
        let objeto_notas = {
            cinco: 0,
            dez: 0,
            vinte: 0,
            cinquenta: 0,
            cem: 0
        }
        let valor_temp = this.valor

        while(valor_temp >= 100 && valor_temp > 0){
            objeto_notas.cem += 1
            valor_temp -= 100
        }
        while(valor_temp >= 50 && valor_temp > 0){
            objeto_notas.cinquenta += 1
            valor_temp -= 50
        }
        while(valor_temp >= 20 && valor_temp > 0){
            objeto_notas.vinte += 1
            valor_temp -= 20
        }
        while(valor_temp >= 10 && valor_temp > 0){
            objeto_notas.dez += 1
            valor_temp -= 10
        }
        while(valor_temp >= 5 && valor_temp > 0){
            objeto_notas.cinco += 1
            valor_temp -= 5
        }
        return `
        ${objeto_notas.cem} nota(s) de cem, 
        ${objeto_notas.cinquenta} nota(s) de cinquenta, 
        ${objeto_notas.vinte} notas(s) de vinte, 
        ${objeto_notas.dez} nota(s) de dez, 
        ${objeto_notas.cinco} nota(s) de cinco`

    }
    possibilidade_2(){
        let objeto_notas = {
            cinco: 0,
            dez: 0,
            vinte: 0,
            cinquenta: 0,
        }
        let valor_temp = this.valor

        while(valor_temp >= 50 && valor_temp > 0){
            objeto_notas.cinquenta += 1
            valor_temp -= 50
        }
        while(valor_temp >= 20 && valor_temp > 0){
            objeto_notas.vinte += 1
            valor_temp -= 20
        }
        while(valor_temp >= 10 && valor_temp > 0){
            objeto_notas.dez += 1
            valor_temp -= 10
        }
        while(valor_temp >= 5 && valor_temp > 0){
            objeto_notas.cinco += 1
            valor_temp -= 5
        }
        return `
        ${objeto_notas.cinquenta} nota(s) de cinquenta,
        ${objeto_notas.vinte} notas(s) de vinte,
        ${objeto_notas.dez} nota(s) de dez,
        ${objeto_notas.cinco} nota(s) de cinco`

    }
    possibilidade_3(){
        let objeto_notas = {
            cinco: 0,
            dez: 0,
            vinte: 0,
        }
        let valor_temp = this.valor

        while(valor_temp >= 20 && valor_temp > 0){
            objeto_notas.vinte += 1
            valor_temp -= 20
        }
        while(valor_temp >= 10 && valor_temp > 0){
            objeto_notas.dez += 1
            valor_temp -= 10
        }
        while(valor_temp >= 5 && valor_temp > 0){
            objeto_notas.cinco += 1
            valor_temp -= 5
        }
        return `
        ${objeto_notas.vinte} notas(s) de vinte,
        ${objeto_notas.dez} nota(s) de dez,
        ${objeto_notas.cinco} nota(s) de cinco`

    }
    possibilidade_4(){
        let objeto_notas = {
            cinco: 0,
            dez: 0,
        }
        let valor_temp = this.valor

        while(valor_temp >= 10 && valor_temp > 0){
            objeto_notas.dez += 1
            valor_temp -= 10
        }
        while(valor_temp >= 5 && valor_temp > 0){
            objeto_notas.cinco += 1
            valor_temp -= 5
        }
        return `
        ${objeto_notas.dez} nota(s) de dez,
        ${objeto_notas.cinco} nota(s) de cinco`

    }
    possibilidade_5(){
        let objeto_notas = {
            cinco: 0,
        }
        let valor_temp = this.valor

        while(valor_temp >= 5 && valor_temp > 0){
            objeto_notas.cinco += 1
            valor_temp -= 5
        }
        return `
        ${objeto_notas.cinco} nota(s) de cinco`

    }
    get mostrar_possibilidades(){
        if (this.valor >= 100){
            return `
Primeira possibilidade: 
            ${this.possibilidade_1()} ||

Segunda possibilidade:
            ${this.possibilidade_2()} ||

Terceira possibilidade: 
            ${this.possibilidade_3()} ||

Quarta possibilidade: 
            ${this.possibilidade_4()} ||

Quinta possibilidade: 
            ${this.possibilidade_5()} ||
            `
            
        }
        else if(this.valor < 100 && this.valor >= 50 ){
            return `
Primeira possibilidade: 
            ${this.possibilidade_2()} ||

Segunda possibilidade: 
            ${this.possibilidade_3()} ||

Terceira possibilidade:
            ${this.possibilidade_4()} ||

Quarta possibilidade: 
            ${this.possibilidade_5()} ||
            `

        }
        else if(this.valor < 50 && this.valor >= 20 ){
            return `
Primeira possibilidade:
            ${this.possibilidade_3()} ||

Segunda possibilidade: 
            ${this.possibilidade_4()} ||

Terceira possibilidade:
            ${this.possibilidade_5()} ||
            `

        }
        else if(this.valor < 20 && this.valor >= 10 ){
            return `
Primeira possibilidade:
            ${this.possibilidade_4()} ||

Segunda possibilidade: 
            ${this.possibilidade_5()}
            `

        }
        else{
            return `
            ${this.possibilidade_5()}
            `

        }
    } 
}

function calculaNotas(e){
    const valor = Number(document.querySelector('.valor').value)
    let resultado = ""
    
    if(valor % 5 != 0 || valor <= 0){
        resultado +=
        `
        <div class="alert alert-danger alert-dismissible fade show" role="alert">
        <strong>Valor inválido!</strong> 
        </div>
        `
    }
    else {
        consulta = new Contador_notas(valor)
        resultado += 
        `
        <div class="alert alert-light alert-dismissible fade show" role="alert">
        <p class ="m-8"><strong>Possibilidades: </strong>${consulta.mostrar_possibilidades}</p>
      </div>
        `
    }
    
    document.querySelector('#notasContadas').innerHTML = resultado
    e.preventDefault()

}