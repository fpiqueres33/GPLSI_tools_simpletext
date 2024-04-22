import re


class Anglicismos:
    def __init__(self, diccionario=None):
        if diccionario is None:
            diccionario = {
                'afterwork': 'Afterwork es una actividad social que hacen compañeros de trabajo fuera del horario laboral.(Gastronomía)',
                'airbnb': 'Empresa que tiene una página web donde las personas pueden ofrecer y reservar lugares para quedarse, como casas o apartamentos, para viajes. (Turismo)',
                'app': 'Aplicación móvil. Una app es una aplicación diseñada para ser usada en teléfonos inteligentes, tabletas y otros dispositivos móviles. (Tecnología)',
                'aquaplanning': 'El aquaplaning sucede cuando un coche va encima de un poco de agua en la carretera. Esto hace que los neumáticos pierdan agarre y control porque no pueden sostenerse bien. (Vehículos)',
                'baby-sitter': 'Canguro. Una niñera o niñero es alguien que cuida a los niños de otra persona. (General)',
                'babysitter': 'Canguro. Una niñera o niñero es alguien que cuida a los niños de otra persona. (General)',
                'babyshower': 'Un babyshower es una fiesta para celebrar que pronto llegará un bebé. Los padres reciben regalos y pasan tiempo con amigos y familiares. (General)',
                'backstage': 'Bambalinas. Backstage se refiere a las áreas y aspectos del espectáculo que no son visibles para el público, como las bambalinas y otros espacios detrás del escenario. (Entretenimiento)',
                'backup': 'Copia de seguridad. Una copia de seguridad es una copia de los datos importantes que se hace para poder recuperarlos si se pierden. (Tecnología)',
                'banner': 'Pancarta. Un banner, también llamado banderola o pancarta, es un tipo de publicidad que se muestra en internet. (Tecnología)',
                'barman': 'Un barman es la persona que sirve a los clientes en la barra de un bar, cervecería, taberna o similar. (Gastronomía)',
                'Batch cooking': 'Preparación de comida. (Gastronomía)',
                'beatbox(ing)': 'Beatboxing es hacer música con la boca. Se hace imitando sonidos de instrumentos como la batería y los platillos. (Música)',
                'best seller': 'Superventas. Un libro, disco, canción o videojuego que mucha gente compra y se vuelve muy popular. (Entretenimiento)',
                'binge-watching': 'Binge-watching significa ver muchos episodios de una serie de televisión seguidos. (Entretenimiento)',
                'biopic': 'Película biográfica. Es un tipo de película que cuenta la vida de una persona real o un grupo de personas, usando actores y dramatización. (Entretenimiento)',
                'blazer': 'Chaqueta deportiva. Un blazer es una chaqueta ajustada al torso con mangas largas, solapas y bolsillos tanto adentro como afuera. Se abre por adelante con botones y se puede llevar abierta o cerrada. (Moda)',
                'blister': 'Envase, Es un envase de plástico transparente con una cavidad que protege el producto y lo muestra en la tienda. (Medicina)',
                'blog': 'Diario. Un blog es como un diario en línea que se actualiza regularmente. Las personas pueden dejar comentarios en las publicaciones del blog, lo que crea una comunidad alrededor del autor o autora. Los blogs son una forma popular de expresarse en internet. (Tecnología)',
                'blogs': 'Diario. Un blog es como un diario en línea que se actualiza regularmente. Las personas pueden dejar comentarios en las publicaciones del blog, lo que crea una comunidad alrededor del autor o autora. Los blogs son una forma popular de expresarse en internet. (Entretenimiento)',
                'bluetooth': 'Es un sistema de radio útil para dispositivos móviles que se usan a corta distancia. (Tecnología)',
                'bodybuilding': 'Culturismo. El culturismo o fisicoculturismo es hacer ejercicio para desarrollar muchos músculos en el cuerpo. (Deporte)',
                'bowl': 'Tazón, cuenco, Un bowl es como un tazón, pero tiene forma semiesférica y no tiene asas. (Gastronomía)',
                'brainstorming': 'Lluvia de ideas. El brainstorming es cuando un grupo de personas se reúne para tener muchas ideas nuevas en un ambiente creativo. (General)',
                'branding': 'Es un diseño gráfico que representa a una empresa y muestra quiénes son desde un punto de vista visual. (General)',
                'break': 'Descanso. Breve suspensión de una actividad. (General)',
                'brunch': 'Brunch eses una comida que se toma a media mañana qy que reemplaza tanto el desayuno como el almuerzo. Proviene de la combinación de "breakfast" (desayuno) y "lunch" (almuerzo).". (Gastronomía)',
                'bullying': 'Acoso escolar. Es cuando alguien hace daño a otra persona muchas veces de diferentes formas, como insultando, golpeando o excluyendo, tanto en la escuela como en internet. (General)',
                'bungalow': 'Bungaló. Tipo de casa de un solo piso con un porche en frente. Se construyen en lugares para relajarse y descansar. (General)',
                'bungee jumping': 'Deporte que consiste en saltar con una cuerda elástica desde una altura elevada. (Deporte)',
                'burger': 'Hamburguesa. (Gastronomía)',
                'burnout': 'Desgaste. Sentirse muy estresado por mucho tiempo debido a problemas emocionales y relaciones difíciles en el trabajo y no poder realizar el bien el trabajo. (General)',
                'cake': 'Pastel, tarta. (Gastronomía)',
                'camping': 'Campamento, acampar. Acampar es cuando pones una casa temporal en un lugar para quedarte. También puede referirse al lugar donde acampas. (Deporte)',
                'cardigan': 'Chaqueta deportiva de punto, con escote en pico, no suele tener cuello. (Moda)',
                'carrot cake': 'Pastel de zanahoria. (Gastronomía)',
                'cash': 'Efectivo. Dinero en forma de monedas o billetes que se utiliza para realizar pagos. (Economía)',
                'casting': 'Audición. Elegir a las personas que actuarán en una película o espectáculo. (Entretenimiento)',
                'catering': 'El servicio de alimentación institucional o colectiva proporciona comida y bebida en eventos y celebraciones. (Gastronomía)',
                'celebrity': 'Celebridad. Una persona famosa (Moda)',
                'chat': 'Un chat es cuando las personas hablan entre sí usando una computadora o teléfono y conexión a Internet. Lo hacen escribiendo mensajes que aparecen instantáneamente en la pantalla del otro (Tecnología)',
                'check-in': 'Registro. Cuando una persona llega a un hotel, estación de tren, aeropuerto o puerto, y un empleado confirma su llegada. (Turismo)',
                'check-out': 'Salida. Cuando una persona deja un hotel y va al mostrador para pagar todo lo que debe. (Turismo)',
                'cheesecake': 'Tarta de queso. (Gastronomía)',
                'chic': 'Elegante, distinguido, a la moda. Manera elegante y de moda de vestir y comportarse (Moda)',
                'click': 'Hacer clic es cuando presionas un botón o una tecla en el ratón. (Tecnología)',
                'coach': 'Entrenador. Coach significa entrenador o preparador, es una palabra en inglés (Deporte)',
                'coaches': 'Entrenadores, entrenadoras. Coach significa entrenador o preparador, es una palabra en inglés (Deporte)',
                'cocktail': 'Cóctel o coctel. Un cóctel es una mezcla de diferentes bebidas. Puede incluir dos o más tipos de bebidas, algunas de las cuales pueden no ser alcohólicas. Se pueden agregar ingredientes como jugos, frutas, miel, leche, crema o especias." . (Gastronomía)',
                'coffee break': 'Recesos o pausa para el café. El coffee break es una pausa durante charlas, reuniones de trabajo o eventos. Durante esta pausa, se ofrece café y pequeños aperitivos a los participantes para descansar. (Gastronomía)',
                'confort': 'Comodidad. Cualquier cosa que te haga sentir bien y puede dificultar que te concentres en lo que necesitas hacer. (General)',
                'cookie': 'Galleta. Cookie es una palabra relacionada con los ordenadores que significa información que un servidor guarda sobre un usuario en su equipo. (Gastronomía)',
                'cookies': 'Cookie es una palabra relacionada con los ordenadores que significa información que un servidor guarda sobre un usuario en su equipo (Tecnología)',
                'cool': 'Guay. Es un estilo, actitud o característica que la gente suele admirar (Moda)',
                'copyright': 'Derecho de autor. Un tipo de protección legal que da a alguien el derecho exclusivo de usar y compartir su obra creativa, como música, libros o películas, por un tiempo limitado. (Entretenimiento)',
                'cover': 'Versión. Un cover es cuando alguien canta o graba una canción que fue hecha por otra persona. También puede ser la parte delantera de un disco o libro. (Música)',
                'coworking': 'Es cuando personas que trabajan solas comparten un lugar de trabajo. Pueden ser independientes, emprendedores o dueños de pequeñas empresas. Comparten un espacio para trabajar juntos en sus proyectos, pero cada uno trabaja en su propia tarea." . (General)',
                'Crossfit': 'Este método de entrenamiento consiste en hacer diferentes ejercicios con barras y movimientos que son útiles en la vida diaria. Se hacen a un ritmo rápido y con mucha energía (Deporte)',
                'crowdfunding': 'Micromecenazgo. Es una forma en la que muchas personas trabajan juntas para financiar proyectos usando nuevas tecnologías. (General)',
                'crush': 'Crush es una palabra usada de manera informal para describir una atracción romántica hacia alguien que puede ser platónica, obsesiva o imposible. (General)',
                'cupcake': 'Magdalena. (Gastronomía)',
                'cycling indoor': 'Es una actividad física en una bicicleta especial que no se mueve. Haces ejercicio aeróbico pedaleando al ritmo de la música. A veces pedaleas rápido, otras veces más despacio, como si estuvieras subiendo una montaña. (Deporte)',
                'derby': 'Clásico deportivo. Derbi es cuando dos equipos juegan un partido y tienen una gran rivalidad porque son de la misma ciudad o región. A veces, equipos de diferentes lugares también tienen rivalidades importantes a nivel nacional. (Deporte)',
                'detox': 'Desintoxicación o limpieza del cuerpo. Significa sacar sustancias dañinas del cuerpo o estar un tiempo sin consumir drogas. (belleza)',
                'disc-jokey': 'Pinchadiscos. pinchadiscos o persona que selecciona y mezcla música grabada propia o de otros compositores y artistas. (Música)',
                'doping ': 'Dopaje. Doping es usar métodos o sustancias prohibidas en el deporte que pueden dañar la salud y mejorar el rendimiento de manera injusta. (Deporte)',
                'download': 'Descargar. La descarga digital es cuando obtienes de internet música para tu dispositivo o datos para tu teléfono móvil. (Tecnología)',
                'ebook': 'Libro electrónico. Dispositivo electrónico que permite almacenar, reproducir y leer libros. (Tecnología)',
                'email': 'Correo electrónico. El correo electrónico es como enviar cartas, pero por internet. (Tecnología)',
                'emails': 'Correos electrónicos. El correo electrónico es como enviar cartas, pero por internet. (Tecnología)',
                'fake': 'Falso. Fake es algo que parece real pero en realidad es falso o una imitación. (General)',
                'fast food': 'Comida rápida. tipo de comida que se prepara y sirve rápidamente en lugares especiales, como restaurantes de la calle o establecimientos de comida rápida. (Gastronomía)',
                'feedback': 'Retroalimentación. Feedback es como recibir comentarios para mejorar. Es cuando una parte de lo que hace un sistema se utiliza para ajustar cómo funciona. (General)',
                'feeling': 'Buena sintonía o simpatía que se establece entre dos o más personas. (General)',
                'ferry': 'Transbordador. Un transbordador, también llamado ferri o ferry, es un barco que lleva personas y a veces coches de un lugar a otro en horarios específicos . (General)',
                'firewall': 'Cortafuegos. Es un programa usado en computadoras para evitar y proteger contra ciertos tipos de comunicaciones que van en contra de las reglas (Tecnología)',
                'fitness': 'Entrenamiento físico. Estar sano y sentirse bien físicamente es resultado de llevar una vida saludable y hacer ejercicio regularmente, de manera constante (Deporte)',
                'food truck': 'Gastroneta. Un food truck es un camión grande que vende comida en la calle. Algunos tienen comida congelada o precocinada, mientras que otros tienen cocinas para preparar platos desde cero. (Gastronomía)',
                'foodie': 'Comidista. Un foodie es alguien a quien le gusta mucho la comida y las bebidas. (Gastronomía)',
                'footing': 'Correr. Es correr a una velocidad moderada al aire libre (Deporte)',
                'freelance': 'Indepentiente, autónomo. Un freelance es una persona que trabaja por su cuenta, sin depender de una empresa. Ofrecen sus servicios a diferentes clientes según su propio horario y condiciones. (General)',
                'frosting': 'Glaseado. El frosting es una cobertura brillante y a menudo dulce que se pone sobre los alimentos. (Gastronomía)',
                'gamer': 'Videojugador. Persona que juega a algún videojuego apasionadamente. (Entretenimiento)',
                'gang ': 'Banda, Banda violenta de criminales. (General)',
                'gangster': 'Malhechor, delincuente, bandido, matón, pistolero, gorila, atracador. Un gánster es un criminal que a menudo se une a una banda violenta llamada "gang" en inglés. (General)',
                'ghosting': 'Es cuando dos personas dejan de hablar en línea sin razón aparente. (Tecnología)',
                'gin': 'Ginebra. Gin es el nombre en inglés de la bebida alcohólica ginebra . (Gastronomía)',
                'glamour': 'Encanto natural que fascina (Moda)',
                'gospel': 'Góspel. Es música religiosa de las comunidades afroamericanas. (Música)',
                'grill': 'Parrilla. cocinar alimentos directamente sobre el calor seco, en una rejilla metálica que deja marcas . (Gastronomía)',
                'hacker': 'Pirata informático. Es alguien que es muy bueno usando computadoras y busca problemas en sistemas informáticos para arreglarlos y mejorarlos. (Tecnología)',
                'handicap': 'Hándicap. El hándicap es un sistema que da ventajas a diferentes competidores para igualar sus oportunidades de ganar en deportes. (Deporte)',
                'hardware': 'Ordenador. Hardware son las partes físicas de una computadora, como el disco duro o la unidad de CD. Son las partes que puedes tocar y ver. CD es Compact Disc o disco compacto. (Tecnología)',
                'hashtag': 'Etiqueta. Un hashtag es una palabra clave que puedes hacer clic. (Tecnología)',
                'healthy': 'Sano. (Gastronomía)',
                'hippie': ' Jipi. Es un grupo de personas que creen en la libertad y la paz. Se hicieron conocidos en los años 60 en Estados Unidos. También se les llama así a las personas que siguen este movimiento. (General)',
                'hippy ': ' Jipi. Es un grupo de personas que creen en la libertad y la paz. Se hicieron conocidos en los años 60 en Estados Unidos. También se les llama así a las personas que siguen este movimiento. (General)',
                'hobbies': 'Pasatiempos. Un hobby es algo que haces por diversión en tu tiempo libre, no como trabajo y sin que te paguen por ello . (General)',
                'hobby': 'Pasatiempo. Un hobby es algo que haces por diversión en tu tiempo libre, no como trabajo y sin que te paguen por ello (Deporte)',
                'hoodie': 'Sudadera. Sudadera con capucha (Moda)',
                'hot dog': 'Perrito caliente. (Gastronomía)',
                'hot pot': 'El hot pot es una comida donde se cocina la comida en un caldo caliente que está en el centro de la mesa. (Gastronomía)',
                'influencer': 'Celebridad de internet. Es alguien que tiene muchas personas que lo siguen en redes sociales como Instagram o YouTube. Estas personas escuchan lo que dice y comparten sus mensajes y recomendaciones. (Moda)',
                'jacuzzi': 'Baño, hidromasaje. Es una bañera con agua caliente que tiene diferentes salidas para llenar y vaciar el agua. (General)',
                'jeans': 'Pantalones vaqueros. tejanos, Tipo de pantalón confeccionado con tela vaquera (Moda)',
                'jet lag': 'Jet lag es cuando te sientes mal después de un largo viaje en avión con cambios en los horarios. Esto hace que tu cuerpo se desajuste. (Turismo)',
                'jumpscare': 'Susto repentino. Un jumpscare es una técnica de asustar que se usa en películas de terror y videojuegos de terror. Consiste en sorprender al espectador con un cambio repentino en la imagen o evento, la mayoría de veecs acompañado de un sonido fuerte y desagradable. (Entretenimiento)',
                'junior': 'Júnior, joven. (General)',
                'ketchup': 'Kétchup. Salsa agridulce hecha de tomates, azúcar, vinagre y especias, que se originó en China . (Gastronomía)',
                'layout': 'Diseño, maquetación. Layout significa organizar texto, imágenes y otros elementos en páginas de libros, periódicos y revista (Tecnología)',
                'lifting': 'Tratamiento estético para estirarse la piel y reducir las arrugas (belleza)',
                'light': 'Light significa que una bebida o comida tiene menos calorías de lo normal. (Gastronomía)',
                'link': 'Enlace, hipervínculo. Un hipervínculo o enlace es una palabra o imagen en un documento electrónico que te lleva a otro lugar cuando haces clic en ella. Puede llevar a otros documentos o partes del mismo documento. (Tecnología)',
                'live': 'Vivo. Producción audiovisual que se transmite en tiempo real, a medida que ocurren los eventos. (Entretenimiento)',
                'lobby': 'Grupo de presión. Es un grupo de personas que comparten intereses similares y trabajan juntas para persuadir al gobierno a tomar decisiones que beneficien a su sector específico de la sociedad. (General)',
                #'lobby': 'Vestíbulo, recepción. Un lobby es una habitación en un edificio utilizado para la entrada desde el exterior . (General)',
                'loft': 'Un loft o desván es un espacio grande con pocos muros, muchas ventanas y mucha luz. (General)',
                'login': 'Inicio de sesión. Una cuenta tiene un nombre de usuario (a veces llamado login) y una contraseña (también llamada password) (Tecnología)',
                'look': 'Imagen, aspecto. Look es una palabra que significa cómo se ve o se viste una persona en inglés. En otros idiomas también se usa para describir la apariencia o estilo de vestir. (Moda)',
                'lunch': 'Almuerzo, refrigerio, aperitivo. Comida ligera . (Gastronomía)',
                'magazine': 'Revista. Publicación que sale regularmente, ya sea para el público en general o para un grupo específico. Profundizan más en los temas que tratan, que pueden ser de actualidad o de entretenimiento. (Entretenimiento)',
                'makeup': 'Maquillaje. Es cuando se usa pintura o cosméticos en el cuerpo para cambiar su apariencia. Puede usarse por razones culturales, sociales o para divertirse . (General)',
                'manager': 'Gerente. Un gerente es la persona encargada de dirigir o coordinar una empresa, grupo, institución o departamento. (General)',
                'marketing': 'Mercadotecnia. En negocios, el mercadeo o marketing es sobre cómo entender, crear y ofrecer cosas que la gente necesita o quiere. (General)',
                'master class': 'Clase magistral. Una clase magistral es una clase impartida a estudiantes de una disciplina específica por un experto en esa disciplina, que puede ser música, ciencia, pintura, drama, juegos u otras ocasiones donde se desarrollen habilidades. (General)',
                'meal prep': 'Preparación de comida. (Gastronomía)',
                'meme': 'Un meme es una imagen o texto gracioso que se comparte en internet. (Entretenimiento)',
                'mobbing': 'Acoso laboral. Es cuando una o más personas tratan de asustar, menospreciar o desanimar a un trabajador. para hacerle daño emocional . (General)',
                'mouse': 'Ratón, también llamado mouse, es un aparato que ayuda a mover cosas en la pantalla de un ordenador. (Tecnología)',
                'muffins': 'Pan redondo con levadura. A menudo está espolvoreado con harina de maíz y se come para el desayuno . (Gastronomía)',
                'newsletter': 'Boletín informativo. Tipo de publicación que se publica regularmente y se enfoca en un tema específico. Muchas asociaciones, negocios y empresas lo utilizan para compartir información importante con sus miembros o empleados. (Tecnología)',
                'offline': 'Fuera de línea. sin conexión, Fuera de línea significa que un equipo está apagado o desconectado de la red. También se dice que alguien está fuera de línea cuando no está usando un ordenador conectado a internet (Tecnología)',
                'online': 'En línea. Estar conectado a internet, mientras que fuera de línea significa estar desconectado. Se usa en computadoras para describir si algo o alguien está conectado a la red, como internet (Tecnología)',
                'outfit': 'Vestimenta, indumentaria. (Moda)',
                'overbooking': 'Sobreventa, sobrecontratación. Overbooking significa que se venden más asientos o habitaciones de las disponibles, en especial en hoteles y aviones . (Turismo)',
                'paddle tennis': 'Pádel. Es un deporte se juega en parejas con una pelota y una pala. Debes hacer botar la pelota en el campo del equipo contrario, usando las paredes y los cristales de la pista si es necesario. (Deporte)',
                'paddle': 'Pádel. Es un deporte se juega en parejas con una pelota y una pala. Debes hacer botar la pelota en el campo del equipo contrario, usando las paredes y los cristales de la pista si es necesario. (Deporte)',
                'panty': 'Panti. Son medias que cubren las piernas por completo, desde la cintura hacia abajo. (Moda)',
                'parking': 'Aparcamiento, estacionamiento. Un parking o estacionamiento es donde se deja un coche por un tiempo. (General)',
                'password': 'Contraseña, clave. Una contraseña o clave es una palabra secreta que se usa para entrar a algo, como una cuenta en línea o un sistema de seguridad (Tecnología)',
                'penalty': 'Penalti. El penalti es una sanción importante en varios deportes con pelota. Consiste en un lanzamiento sin barrera hacia el gol desde una distancia específica, con solo el portero como oposición. (Deporte)',
                'pendrive': 'El pendrive es un dispositivo pequeño que guarda información usando chips en lugar de partes móviles. (Tecnología)',
                'personal shopper': 'Persona que asesora y ayuda a una persona (o grupo de personas) a transformar su imagen. (Moda)',
                'personal trainer': 'Entrenador personal. Un entrenador personal es alguien con mucha formación sobre hacer ejercicio. Le enseña a la gente qué ejercicios hacer y cómo hacerlos correctamente. (Deporte)',
                'picnic': 'Comida informal al aire libre. (Gastronomía)',
                'ping-pong': 'Pimpón, tenis de mesa. Es un juego parecido al tenis que se juega en una mesa con una pelota ligera y palas pequeñas de madera en lugar de raquetas (Deporte)',
                'pit lane': 'Calle de garajes. Es una pista que conecta el circuito con el área de garajes. Suele estar al lado de la recta principal del circuito. (Deporte)',
                'playlist': 'Lista de reproducción. Lista de canciones. (Música)',
                'plot twist': 'Giro argumental, Un plot twist es una técnica literaria que introduce un cambio importante en la dirección o resultado esperado de la trama en una obra de ficción. Cuando ocurre cerca del final de la historia, se conoce como un giro o final sorpresa. (Entretenimiento)',
                'podcast': 'Un pódcast es una serie de archivos que puedes escuchar en línea o descargar en tu dispositivo. (Entretenimiento)',
                'Poke bow': 'Ensalada de pescado crudo de Hawái. (Gastronomía)',
                'pole position ': 'Primera posición. Es el primer lugar en la línea de salida de una carrera de automovilismo o motociclismo (Deporte)',
                'portfolio': 'Portafolio, Colección de los mejores trabajos de un artista o profesional, ya sea en formato físico o digital. Se muestra a los clientes para que vean el tipo de trabajo que hace y, con suerte, decidan contratarlo . (General)',
                'post': 'Publicación. (Tecnología)',
                'powerlifter': 'Persona que practica el deporte powerlifting (Deporte)',
                'powerlifting': 'Levantamiento de potencia. El powerlifting es un deporte de fuerza donde se hacen tres ejercicios: la sentadilla, el press de banca y el peso muerto. (Deporte)',
                'prime time': 'Horario de máxima audiencia. Es un período de tiempo en la televisión que tiene programas adecuados para toda la familia. (Tecnología)',
                'pub': 'Bar, Es un lugar donde se venden y sirven bebidas alcohólicas, de acuerdo con las leyes del país. (Gastronomía)',
                'puenting': 'Deporte que consiste en saltar con una cuerda elástica desde una altura elevada (Deporte)',
                'pulled pork': 'El pulled pork es una comida de Estados Unidos que consiste en cerdo desmenuzado o deshilachado. (Gastronomía)',
                'ranking': 'Clasificación. Es ordenar a las personas o cosas según sus características o cualidades, siguiendo el criterio de quien lo hace. (General)',
                'rating': 'Valoración. (Tecnología)',
                'relax': 'Relajación, calma, tranquilidad. (General)',
                'remake': 'Nueva versión. Es una nueva versión de una película que sigue muy de cerca la historia, personajes y escenarios de la versión anterior. (Entretenimiento)',
                'remaster': 'Es cuando se mejora el sonido o la calidad visual de una grabación antigua usando tecnología digital. También se puede referir a crear una nueva versión de una obra grabada . (Entretenimiento)',
                'remix': 'Remezcla. Un remix es cuando cambias una canción para que suene diferente o mejor. (Música)',
                'resort': 'Complejo turístico, complejo hotelero, centro vacacional o resorte. Un resort es un lugar diseñado para que la gente se relaje y se divierta durante las vacaciones. Ofrece muchas actividades como comida, alojamiento, deportes y entretenimiento. (Turismo)',
                'ring': 'Cuadrilátero, lona. Lugar donde se pelean en deportes como el boxeo, artes marciales mixtas y lucha libre. Es como un cuadrilátero o una lona. (Deporte)',
                'runner': 'Corredor. Persona que corre y participa en carreras (Deporte)',
                'safety car': 'Coche de seguridad. Coche especial que se usa en las carreras para detener la carrera cuando hay un accidente o mal tiempo y reunir a todos los competidores (Deporte)',
                'self-service': 'ASutoservicio. Self-service significa que el cliente elige y recoge sus propias cosas en la tienda, en lugar de que un empleado lo haga. Es diferente de las tiendas donde te ayudan a encontrar los productos. (Turismo)',
                'selfie': 'Autofoto, selfi. Un selfi es una foto que te tomas a ti mismo con una cámara. (Tecnología)',
                'selfies': 'Autofotos. (Tecnología)',
                'share': 'Cuota de pantalla. Es una medida que muestra qué parte de las personas que están viendo la televisión están viendo un programa en particular, comparado con el total de personas que tienen la televisión encendida en ese momento. (Tecnología)',
                'shopping': 'Cuando una persona mira los productos o servicios que ofrecen una o más tiendas con la posibilidad de comprar algo. (General)',
                'short': 'Pantalón corto. Short es un pantalón corto que usan hombres y mujeres. Cubre las piernas desde la cintura, pero solo de manera parcial. (Moda)',
                'shortpitch': 'Es una actividad de la industria audiovisual de las películas cortas. Pueden participar directores o productoras del país. (Entretenimiento)',
                'shorts': 'Pantalones cortos. Short es un pantalón corto que usan hombres y mujeres. Cubre las piernas desde la cintura, pero solo de manera parcial. (Moda)',
                'show': 'Espectáculo. (Entretenimiento)',
                'skateboard': 'Monopatín, patineta, patinete o tabla de patinaje. El monopatín es una tabla larga con cuatro ruedas. Se utiliza para practicar el deporte llamado monopatinaje (Deporte)',
                'skater': ' Patinaje con monopatín. (Deporte)',
                'skyline': 'Línea del horizonte. Skyline es la vista de los edificios más altos de una ciudad, como los rascacielos, que forman su silueta o perfil. . (General)',
                'slip': 'Es una prenda interior ajustada que sujeta los órganos genitales en su lugar. Puede tener o no una abertura en la parte frontal (Moda)',
                'smartphone': 'Teléfono inteligente, también conocido como smartphone, es un tipo de teléfono móvil que hace muchas cosas además de llamar, como unir un teléfono y un ordenador de bolsillo. (Tecnología)',
                'Smoothie': 'Un batido es una bebida hecha mezclando ingredientes en una licuadora. (Gastronomía)',
                'snack': 'Aperitivos. Los snacks son alimentos que se comen para calmar el hambre, dar un poco de energía al cuerpo o simplemente por placer . (Gastronomía)',
                'snorkel': 'Esnórquel. El esnórquel es un tubo que se usa para respirar bajo el agua. (Deporte)',
                'software': 'Programa de ordenador. El software es como el cerebro de una computadora. Es el conjunto de instrucciones que hacen que la computadora funcione y realice tareas. Esto es diferente del hardware, que son las partes físicas de la computadora (Tecnología)',
                'sold out': 'Agotado. Que no hay más entradas o productos disponibles para comprar . (General)',
                'soundtrack': 'Banda sonora. La banda sonora es todo lo que se escucha en una película o programa de televisión, como diálogos, música y sonidos ambientales. (Entretenimiento)',
                'spam': 'Correo basura. correo no deseado, Es una nueva manera de enviar anuncios no deseados a las personas a través de correo, redes sociales o foros, sin que las personas lo hayan pedido. (Tecnología)',
                'speech': 'Discurso. Speech es hablar frente a una audiencia. Puede ser en persona o a través de tecnología, como un discurso grabado. (Tecnología)',
                'spinning': 'Es una actividad física en una bicicleta especial que no se mueve. Haces ejercicio aeróbico pedaleando al ritmo de la música. A veces pedaleas rápido, otras veces más despacio, como si estuvieras subiendo una montaña. (Deporte)',
                'spoiler': 'Destripe. Descripción de una parte importante de la trama de un programa de televisión, película, libro, etc . (Entretenimiento)',
                'sponsor': 'Patrocinador. Un patrocinador es una persona o una empresa que apoya una actividad. (Deporte)',
                'spot': 'Anuncio. Spot o spot publicitario es un anuncio corto que se muestra en la radio o la televisión. (Entretenimiento)',
                'sprint': 'Esprint. Aceleración que realiza un corredor en un tramo determinado de la carrera, especialmente en la llegada a meta para disputar la victoria a otros corredores. (Deporte)',
                'startup': 'Empresa emergente. Son empresas nuevas que suelen ser creadas por personas emprendedoras, a menudo basadas en tecnología e ideas innovadoras, y se espera que crezcan rápido. . (General)',
                'steak tartar': 'Filete. Un steak o filete es un trozo de carne roja cortado en forma de filete para comer. (Gastronomía)',
                'Steak ': 'Filete de ternera. (Gastronomía)',
                'stock': 'Existencias. Son los objetos que una empresa tiene para vender o usar en su trabajo diario. (Economía)',
                #'stock': 'existencias, Stock son los productos que una empresa fabrica y vende, o que otras empresas pueden usar. También se les llama mercaderías o existencias comerciales. . (General)',
                'stop and go': 'Pare y siga. Castigo que consiste en que el piloto debe entrar en boxes y quedarse ahí 10 segundos sin poder hacer nada. (Deporte)',
                'stopmotion': 'Son muchas fotos unidas que parece un vídeo . (Entretenimiento)',
                'streaming': 'Traducido al español de diferentes formas, como transmisión de vídeo, transmisión en directo,​ retransmisión o emisión en continuo. (Tecnología)',
                'street food': 'Street food es la comida que se vende en la calle en puestos portátiles o improvisados. (Gastronomía)',
                'sweater': 'Suéter. Un suéter es una prenda de punto con mangas que llega hasta la cintura. (Moda)',
                'tablet': 'Tableta. Dispositivo electrónico portátil más grande que un teléfono. Tiene una pantalla táctil que emite luz y se usa con los dedos o un lápiz óptico (Tecnología)',
                'take away': 'Comida para llevar. (Gastronomía)',
                'target': 'Público objetivo. Público al que se dirige una acción de publicidad (Economía)',
                'targets': 'Público objetivo. Público al que se dirige una acción de publicidad (Economía)',
                'team': 'Equipo, grupo de personas que trabajan juntas. Se comunican, comparten ideas y colaboran para lograr un objetivo que todos quieren alcanzar. (Deporte)',
                'teaser tráiler': 'Un tráiler o teaser es un video corto sobre una película, programa de televisión, o videojuego. Suele publicarse mucho antes del lanzamiento del producto. (Entretenimiento)',
                'teaser': 'Un tráiler o teaser es un video corto sobre una película, programa de televisión, o videojuego. Suele publicarse mucho antes del lanzamiento del producto. (Entretenimiento)',
                'test': 'Prueba o exámen de conocimientos . (General)',
                'tester': 'Probador. Producto de muestra que se usa para saber si te gusta el producto antes de comprarlo. (General)',
                'thriller': 'Suspense. Es un tipo de historia que mantiene a la gente interesada y nerviosa sobre lo que pueda suceder a los personajes y cómo se resolverá el problema. (Entretenimiento)',
                'top model': 'Supermodelo. Es alguien que trabaja como modelo y gana mucho dinero y fama en todo el mundo. (Moda)',
                'top models': 'Supermodelo. Es alguien que trabaja como modelo y gana mucho dinero y fama en todo el mundo. (Moda)',
                'topless': 'Toples. Mujer desnuda de cintura para arriba en lugares públicos como playas o piscinas, usando solo la parte de abajo del bikini (Moda)',
                'top-less': 'Toples.Mujer desnuda de cintura para arriba en lugares públicos como playas o piscinas, usando solo la parte de abajo del bikini (Moda)',
                'topping': 'Se refiere a cualquier ingrediente que se añade encima de otro alimento, como por ejemplo, los ingredientes que se ponen sobre helados, pasteles, pizzas, etc. Es lo que está en la parte superior del alimento y le da sabor o decoración. (Gastronomía)',
                'toppings': 'Se refiere a cualquier ingrediente que se añade encima de otro alimento, como por ejemplo, los ingredientes que se ponen sobre helados, pasteles, pizzas, etc. Es lo que está en la parte superior del alimento y le da sabor o decoración. (Gastronomía)',
                #'trailer': 'avance, Vídeo que presenta un resumen de una película, una serie de televisión, un videojuego o un videoclip. (Entretenimiento)',
                #'trailer': 'remolque, Es un remolque que se conecta y apoya en la parte delantera de un vehículo tractor . (General)',
                'trending topic': 'Tendencia. Tema de tendencia o tema del momento, Un trending topic es una palabra o frase muy mencionada en las redes sociales en un momento específico. (Tecnología)',
                'trendy': 'De moda, tendencia. (Moda)',
                'upgrade': 'Actualización. (Tecnología)',
                'vlog': 'Videoblog. Es como una colección de videos que las personas publican en línea. Los videos se muestran en orden desde el más reciente al más antiguo. (Entretenimiento)',
                'webcam': 'Cámara web. Una cámara web, también llamada webcam, es una pequeña cámara digital que se conecta a un ordenador y puede hacer fotos o videos. Estas imágenes se pueden compartir en internet con otras personas o en una página web. (Tecnología)',
                'wellness': 'Bienestar. significa sentirse bien en todos los aspectos: mental, físico y emocional. Cuando tenemos un buen equilibrio en estos aspectos, nos sentimos bien en general. (Deporte)',
                'western  ': 'Wéstern. Western es una palabra que viene del inglés y significa del oeste. Se usa principalmente para hablar de películas, aunque también se usa en libros (novelas del Oeste). (Entretenimiento)',
                'wifi': 'Conexión inalámbrica. Cuando los dispositivos se conectan usando ondas electromagnéticas en lugar de cables. (Tecnología)',
                'workshop': 'Taller. (General)',
                'wrap': 'Un wrap es como un taco o burrito, pero con ingredientes de sándwich dentro de una tortilla o pan plano. (Gastronomía)'

            }

        self.diccionario = diccionario

    def sustituir_anglicismos(self, texto):
        # Reemplaza los anglicismos en el texto por sus traducciones
        anglicismos_ordenados = sorted(self.diccionario.keys(), key=len, reverse=True)
        texto_original = texto  # Guardamos el texto original para preservar las mayúsculas
        texto = texto.lower()  # Trabajamos con una versión en minúsculas del texto para la búsqueda

        for anglicismo in anglicismos_ordenados:
            inicio = 0
            while inicio < len(texto):
                inicio = texto.find(anglicismo.lower(), inicio)
                if inicio == -1:
                    break
                fin = inicio + len(anglicismo)
                if (inicio == 0 or not texto[inicio - 1].isalnum()) and (fin == len(texto) or not texto[fin].isalnum()):
                    # Verificar si la palabra en el texto original estaba capitalizada
                    if texto_original[inicio].isupper():
                        reemplazo = self.diccionario[anglicismo.lower()].capitalize()
                    else:
                        reemplazo = self.diccionario[anglicismo.lower()]

                    texto_original = texto_original[:inicio] + reemplazo + texto_original[fin:]
                    texto = texto[:inicio] + reemplazo.lower() + texto[
                                                                 fin:]  # Actualizamos también la versión en minúsculas para mantener la coherencia
                    inicio += len(reemplazo)
                else:
                    inicio += len(anglicismo)
        return texto_original


    def detectar_anglicismos(self, texto):
        # Detecta anglicismos en el texto y los devuelve capitalizados si se encuentran
        anglicismos_detectados = []
        anglicismos_ordenados = sorted(self.diccionario.keys(), key=len, reverse=True)
        for anglicismo in anglicismos_ordenados:
            inicio = 0
            while inicio < len(texto):
                inicio = texto.lower().find(anglicismo.lower(), inicio)
                if inicio == -1:
                    break
                fin = inicio + len(anglicismo)
                if (inicio == 0 or not texto[inicio - 1].isalnum()) and (fin == len(texto) or not texto[fin].isalnum()):
                    anglicismos_detectados.append(anglicismo.capitalize())
                    inicio += len(anglicismo)
                else:
                    inicio += len(anglicismo)
        return anglicismos_detectados

    def glosario_anglicismos(self, texto):
        # Usar expresiones regulares para dividir el texto en palabras, ignorando la puntuación
        texto_tokens = re.findall(r'\b\w+\b', texto.lower())
        anglicismos_ordenados = sorted(self.diccionario.keys(), key=len, reverse=True)
        glosario_list = []

        for anglicismo in anglicismos_ordenados:
            anglicismo_lower = anglicismo.lower()
            for token in texto_tokens:
                if anglicismo_lower == token:
                    entrada_glosario = f"{anglicismo.capitalize()}: {self.diccionario[anglicismo]}"
                    if entrada_glosario not in glosario_list:  # Evita duplicados en el glosario
                        glosario_list.append(entrada_glosario)
                    # No es necesario el break aquí, ya que queremos encontrar todos los anglicismos

        return glosario_list