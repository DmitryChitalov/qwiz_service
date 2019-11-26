let qwestions = []
let counter = 0
let points = 0
let ranks = [
            ['quizмагистр','static/img/quizmage.jpg','Ты знаешь все о квизах, потому что играшь постоянно. В твоем городе нет такого квиза, в который бы ты не сыграл хоть однажды. Возможно, ты - игрок одной из легендарных команд, а может даже капитан своей команды! К твоему мнению прислушиваются друзья, а коллеги считают тебя супер профессионалом. В сферу твоих интересов попадает информация от простых новостей до великих научных открытий. Твой кругозор не ограничивается поверхностными заниями, ты всегда докапываешься до истины. Со своей командой ты спокойно и уверенно обосновался в "лиге победителей". Вероятно, Мегаполис Квиз покажется тебе "легким" орешком! Попробуй...'],
            ['Азартный игрок','static/img/player.jpg','Тебе всегда было интересно оказаться на месте игроков "Что? Где? Когда?" или придумать для них каверзный вопрос. Ты любишь различные телевикторины от "Сто к одному" до "Своя игра". В процессе просмотра постоянно соревнуешься с игроками, но не расстраиваешься, если не знаешь правильного ответа, а пополняешь свою копилку знаний. Ты одним из первых узнал о квизах - массовых интеллектуальных играх, доступных для всех. Кажется уже сто лет назад ты впервые сыграл в квиз и понеслось! Ты активно вовлекаешь своих друзей, коллег и знакомых в эту игру, а сам являешься участником разных команд. Любишь соревновательный дух и конечно, всегда стремишься к победе! Приходи к нам и попади в призовую тройку Мегаполис Квиз!'],
            ['Любитель','static/img/middle.jpg','Для тебя игра в квиз - это увлекательный вечер с друзьями: потренировать память, вспомнить классику кино или мировые хиты да и просто пообщаться. Ты вполне объективно оцениваешь свои знания и очень бурно радуешься, когда твой ответ оказывается верным, а таких ответов не так уж и мало. Особенно любишь тематические игры, которые порой сопровождаются костюмированными вечеринками. Часто со своей командой получаешь поощрительные призы и нет ничего прекрасней этой бутылочки шампанского за предпоследнее место или золотую середину! Ведь для тебя важна не победа, а участие! Мегаполис Квиз готов подарить тебе познавательный вечер с друзьями - собирай команду и приходи за новыми впечатлениями!'],
            ['новичёк','static/img/newman.jpg','Ты не знаешь, что такое квиз или считаешь, что это тоже самое, что квест. Об этой игре что-то слышал от друзей, или даже кто-то из них приглашал тебя поиграть. Но ты почему-то стесняешься, боишься, что тебя сочтут дурачком или необразованным. Слушая свои страхи, ты многое теряешь! Сыграв в Мегаполис Квиз, ты удивишься, насколько много ты знаешь, а сколько еще неизведанных тем и фактов!']
           ]

function hide(name) {
      document.getElementById(name).style.display='none';
      }

function show(name,form='block') {
        document.getElementById(name).style.display=form;
    }

function set_rank(i){
    document.getElementById('rank-name').innerHTML = ranks[i][0];
    document.getElementById('rank-description').innerHTML = ranks[i][2];
    document.getElementById('rank-img').src =ranks[i][1]
    }

function next(i){
    document.getElementById('qwestion').innerHTML = qwestions[i]["qwestion"];
    document.getElementById('answ-a').innerHTML = qwestions[i]["a"];
    document.getElementById('answ-b').innerHTML = qwestions[i]["b"];
    document.getElementById('answ-c').innerHTML = qwestions[i]["c"];
    document.getElementById('answ-d').innerHTML = qwestions[i]["d"];
}

function qwiz_select(num){
            $.ajax({
                url: "qwestions/" + num + "/",
                success: function (data) {
                    qwestions = data["result"]
                    hide("qwiz")
                    show("unswers")
                    next(counter)
                },
            });
        }

function clikansw(a) {
    points += qwestions[counter]["p_"+a]
    if (counter<qwestions.length-1) {
        counter++
        next(counter);
    } else {
        hide("unswers");
        show("rank", 'flex')
        let rank = (points/(qwestions.length*4))*100
        console.log(points)
        if (rank>75){
            set_rank(0)
        } else if (rank>50){
            set_rank(1)
        } else if (rank>25){
            set_rank(2)
        } else{
            set_rank(3)
        }
        console.log(rank)
    }
}

window.onload = function ()  {


}