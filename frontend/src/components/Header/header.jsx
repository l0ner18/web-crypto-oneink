import style from './header.module.scss'

const Header = () => {
    return (
        <div className={style.container}>
            <div className={style.container2}>
                <div className={style.container_links}>
                    <div className={style.links}>
                        <div className={style.item}><a href="/" className={style.link}>Главная</a></div>
                        <div className={style.item}><a href="YASH" className={style.link}>YASH</a></div>
                        <div className={style.item}><a href="S-DES" className={style.link}>S-DES</a></div>
                        <div className={style.item}><a href="S-AES" className={style.link}>S-AES</a></div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Header;