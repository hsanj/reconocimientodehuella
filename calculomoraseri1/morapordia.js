let fechaEntrega = new Date('09/12/2021'); //fecha en la que entregan la pelicula, MES/DIA/AÑO
let fechaVencimiento = new Date('10/12/2021');//fecha desde que se empiza a cobrar mora

let milisegundosDia = 24*60*60*1000;

let milisegundosTranscurridos = Math.abs(fechaEntrega.getTime() - fechaVencimiento.getTime());

let diasTranscurridos = Math.round(milisegundosTranscurridos/milisegundosDia);



totalPagar=diasTranscurridos*20;

console.log("TOTTAL A PAGAR:"+totalPagar);