<template >
 <div class="container-fluid d-flex justify-content-center">
    <div class="card  tarjeta   border-info mb-3" >
     <div class="card-header bg-info ">Conversacion</div>
       <div class="card-body" id="cuerpo">
          <div id="tabla" ref="chatbot" name="cajita">
             <table  id ="chat-tabla"  >    
                <tr  class="d-flex flex-column">
                      <td>     
                          <button  v-on:click="servicios" type="button" class="btn btn-info">Nuestros Servicios</button>
                          <button  v-on:click="sandalias" type="button" class="btn btn-info">Sandalias</button>     
                          <button  v-on:click="zapatos" type="button" class="btn btn-info">zapatos</button>     
                          <button  v-on:click="zapatillas" type="button" class="btn btn-info">Zapatillas</button>                 
                     </td>
                    </tr> 
                  <div v-for="(lista,index) in listaMensajes" :key="index">
                    <tr class="d-flex flex-row-reverse "  >
                        <td >
                          <div><span class=" badge badge-success mb-1  ">
                            <h4 class="card-title">Usuario: </h4>{{lista.usuario}} </span>
                            </div>
                        </td>
                    </tr>         
                    <tr  class="d-flex flex-row">
                        <td >
                          <div ><span class="badge badge-secondary">
                            <h4 class="card-title">Boot:</h4> {{lista.boot}}</span>
                            </div> 
                        </td>
                    </tr>  
                   <tr  class="d-flex flex-row">
                      <td>
                            <div v-html="lista.imagenes" class="d-flex ">
                            </div>                  
                     </td>
                    </tr> 
                  </div>                         
             </table>
          </div>
      </div>
        <form @submit.prevent="getMensajeChatbot" class="bg-info">
        <input type="text"   v-model="mensaje_usuario" name="mensaje_usuario" placeholder="Escribe el mensaje..."> 
        <button type="submit" >Enviar</button>
        </form>
  
    </div>
</div>


</template>


<script>
import axios from "axios";
export default {
  name: "Main",
  data() {
    return {
      listaMensajes: [],
      mensaje: "",
      mensaje_bot: "",
      mensaje_boton: "",
    };
  },
  methods: {
    getMensaje() {
      const path = "http://localhost:5000/api/chatbot";
      axios
        .get(path)
        .then((respuesta) => {
          this.mensaje = respuesta.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getMensajeChatbot() {
      // var config = {headers: {"Content-Type": "application/json"}}
      var mensajeUsuario =  { user: this.mensaje_usuario };

      console.log(mensajeUsuario);
      const path = "http://localhost:5000/api/mensaje_chatbot";
      axios
        .post(path, mensajeUsuario)
        .then((respuesta) => {
          var codigo = "";

          if ("tigre" == respuesta.data.boot) {
            this.mensaje_bot =
              "Ofrecemos los siguientes modelos de zapatillas tigre:";
            codigo =
              ' <div class="p-2"><a type="button" class="btn btn-sm btn-info" href="https://www.calzadosportuguez.tk/product/zapatillas-tigre"target="_blank" >   <img src="https://cdn.discordapp.com/attachments/720103348048756797/738520281886228590/aster.jpg" class="img-fluid" alt="..." class="img-thumbnail"></a> </div> ';
          } else if ("zapatillas" == respuesta.data.boot) {
            codigo =
              ' <div class="p-2"><a type="button" class="btn btn-sm btn-info" href="https://www.calzadosportuguez.tk/product/zapatillas-tigre"target="_blank" >  <img src="https://cdn.discordapp.com/attachments/720103348048756797/738548117649227816/walon.png" class="img-fluid" alt="..." class="img-thumbnail"> </a></div> <div>   <div class="p-2"><a type="button" class="btn btn-sm btn-info" href="https://www.calzadosportuguez.tk/product/zapatillas-tigre"target="_blank" > <img src="https://cdn.discordapp.com/attachments/720103348048756797/738548123932033024/walonnegro.png" class="img-fluid" alt="..." class="img-thumbnail"></a></div> <div class="p-2"><a type="button" class="btn btn-sm btn-info" href="https://www.calzadosportuguez.tk/product/zapatillas-tigre"target="_blank" > <img src="https://cdn.discordapp.com/attachments/720103348048756797/738548174343372880/tigre.jpg" class="img-fluid" alt="..." class="img-thumbnail">  </a>  </div>';
            this.mensaje_bot = "le mostramos la siguientes zapatillas";
          } else if ("nike" == respuesta.data.boot) {
            codigo =
              '  <div class="p-2"><a type="button" class="btn btn-sm btn-info" href="https://www.calzadosportuguez.tk/product/zapatillas-tigre"target="_blank" > <img src="https://cdn.discordapp.com/attachments/720103348048756797/738520281886228590/aster.jpg" class="img-fluid" alt="..." class="img-thumbnail"> </a></div>';
            this.mensaje_bot =
              "Ofrecemos los siguientes modelos de zapatillas nike: ";
          } else if ("sandalias" == respuesta.data.boot) {
            codigo =
              ' <div class="p-2"> <a type="button" class="btn btn-sm btn-info" href="https://www.calzadosportuguez.tk/product/import-placeholder-for-154"target="_blank" >  <img src="https://cdn.discordapp.com/attachments/720103348048756797/738548081678745600/trica_roojo.jpg" class="img-fluid" alt="..." class="img-thumbnail"> </a></div> <div class="p-2">    <a type="button" class="btn btn-sm btn-info" href="https://www.calzadosportuguez.tk/product/import-placeholder-for-154e"target="_blank" >     <img src="https://cdn.discordapp.com/attachments/720103348048756797/738548087097655366/trica_azul.jpg" class="img-fluid" alt="..." class="img-thumbnail">  </a>  </div><div class="p-2">  <a type="button" class="btn btn-sm btn-info" href="https://www.calzadosportuguez.tk/product/import-placeholder-for-154"target="_blank" >          <img src="https://cdn.discordapp.com/attachments/720103348048756797/738548052981317672/hello_rosa.jpg" class="img-fluid" alt="..." class="img-thumbnail"> </a></div>';
            this.mensaje_bot = "Ofrecemos los siguientes modelos de sandalia:";
          } else if ("catalogo_sandalias" == respuesta.data.boot) {
            codigo =
              '   <div class="p-2"><a type="button" class="btn btn-sm btn-info" href="https://www.calzadosportuguez.tk/product/zapatillas-tigre"target="_blank" ><img src="https://cdn.discordapp.com/attachments/720103348048756797/738520281886228590/aster.jpg" class="img-fluid" alt="..." class="img-thumbnail">     </a>   </div>';
            this.mensaje_bot =
              "En el siguiente link le mostramos la variedad de sandalias que ofrecemos :";
          } else if ("zapatos" == respuesta.data.boot) {
            codigo =
              '  <div class="p-2"><a type="button" class="btn btn-sm btn-info" href="https://www.calzadosportuguez.tk/product/zapatillas-tigre"target="_blank" >     <img src="https://cdn.discordapp.com/attachments/720103348048756797/738520281886228590/aster.jpg" class="img-fluid" alt="..." class="img-thumbnail">            </a>     </div>';
            this.mensaje_bot = "Ofrecemos los siguientes modelos de zapatos:";
          } else if ("catalogo_zapatilla" == respuesta.data.boot) {
            codigo =
              ' <div class="p-2"><a type="button" class="btn btn-sm btn-info" href="https://www.calzadosportuguez.tk/product/zapatillas-tigre"target="_blank" >   <img src="https://cdn.discordapp.com/attachments/720103348048756797/738520281886228590/aster.jpg" class="img-fluid" alt="..." class="img-thumbnail"> </a>  </div>';
            this.mensaje_bot =
              "En el siguiente link le mostramos la variedad de zapatillas que ofrecemos :";
          } else if ("catalogo_zapato" == respuesta.data.boot) {
            codigo =
              ' <div class="p-2"><a type="button" class="btn btn-sm btn-info" href="https://www.calzadosportuguez.tk/product/zapatillas-tigre"target="_blank" >   <img src="https://cdn.discordapp.com/attachments/720103348048756797/738520281886228590/aster.jpg" class="img-fluid" alt="..." class="img-thumbnail">   </a>   </div>';
            this.mensaje_bot =
              "En el siguiente link le mostramos la variedad de sandalias que ofrecemos :";
          } else {
            this.mensaje_bot = respuesta.data.boot;
          }
          this.listaMensajes.push({
            usuario: respuesta.data.user,
            boot: this.mensaje_bot,
            imagenes: codigo,
          });

          setTimeout(
            function () {
              this.scrollToEnd();
            }.bind(this),
            100
          );

          /* 
            this.mensaje_bot =respuesta.data
             */
        })
        .catch((error) => {
          console.error(error);
        });
    },
    scrollToEnd() {
      var container = this.$refs.chatbot;
      container.scrollTop = container.scrollHeight;
      console.log("Arriba y muy lejos");
    },
    servicios() {
      this.mensaje_boton = "pregunta1";
      getMensajeChatbot();
      this.mensaje_boton = "";
      console.log(this.mensaje_boton);
    },
    zapatos() {
      this.mensaje_boton = "pregunta2";
      getMensajeChatbot();
      this.mensaje_boton = "";
      console.log(this.mensaje_boton);
    },
    zapatillas() {
      this.mensaje_boton = "pregunta 3";
      getMensajeChatbot();
      this.mensaje_boton = "";
      console.log(this.mensaje_boton);
    },
    sandalias() {
      this.mensaje_boton = "pregunta 3";
      getMensajeChatbot();
      this.mensaje_boton = "";
      console.log(this.mensaje_boton);
    },
    created() {
      this.getMensaje();
    },
  },
};
</script>

<style lang="css" scoped>
</style>