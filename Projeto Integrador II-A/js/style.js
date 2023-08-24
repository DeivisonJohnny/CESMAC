const iconMenu = document.querySelector('.bi-list')


iconMenu.addEventListener('click', () => {
    const listMenu = document.querySelector('.listMenu')
    if (listMenu.className == 'listMenu') {
        listMenu.classList.add('menu')
        listMenu.style.animationName = 'openMenu'
    } else {
        listMenu.style.animationName = 'exitMenu'
        setTimeout(() => {
            listMenu.classList.remove('menu')
        }, 280)

    }
})


window.addEventListener('load', () => {
    const bg = document.querySelectorAll('.efeitoBg')
    console.log(bg)
    var grau = 360
    let i = 0
    bg.forEach(index => {
        setInterval(() => {
            if (grau > i) {
                console.log(i)
                index.style.backgroundImage = 'linear-gradient('+ i +'deg, #13005e, #00bfff)'
                i++
            } else {
                i = 0
            }

        }, 50)

    })
})