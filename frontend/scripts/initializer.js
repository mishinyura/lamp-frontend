const page = new Page()

async function productsInit() {
    page.addElement(new Cart, "cart")
    let menu = new TopMenu('menu')
    page.addElement(menu, "topmenu")
    page.addElement([], "cards")

    let products = await request(
        `${SERVER}/products`
    )

    for (let product of products) {
        let card = new Card('cards', product)
        page.objects.cards.push(card)
    }

    // for (let card of page.objects.cards) {
    //     card.buyBtn.addEventListener('click', () => card.addProduct())
    // }

    menu.burger.addEventListener('click', () => menu.editState())
}


const cartInit = () => {
    page.addElement(new Cart, "cart")

    // for (let btn of page.doc.querySelectorAll('.product__down')) {
    //     btn.addEventListener('click', editAmountPositionInCart)
    // }

    // for (let btn of page.doc.querySelectorAll('.product__up')) {
    //     btn.addEventListener('click', editAmountPositionInCart)
    // } 
}

async function adminInit() {
    let products = await request(
        `${SERVER}/products`
    )

    const admin = new Admin("cards"); // если контейнер .admin__list
    await admin.generateItems();
}