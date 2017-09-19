#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <fcntl.h>
#include <linux/ioctl.h>
#include <linux/i2c-dev.h>

int i2c_fd;
FILE *fp;

void ctrl_c(int sig)//e chamada quando control+c e pressionado
{
        printf("\nCtrl+c pressionado, fechando programa\n");
        fclose(fp);//fecha
        close(i2c_fd);//fecha
        exit(-1);
}


int main(void)
{
        signal (SIGINT, ctrl_c);//chama ctrl_c quando se pressiona control c
        unsigned char user_input=1, arduino_ret, rpi_addr = 0xDA, slave_addr = 0x0F;
        float recebe;
        i2c_fd = open("/dev/i2c-1", O_RDWR); //abre o arquivo i2c que permite comunicacao
        ioctl(i2c_fd, I2C_SLAVE, slave_addr); //define o endere  o 0x0F como slave, e o rpi como master
        fp = fopen("arquivo.txt", "w");
        if(!fp)//apenas caso nao seja possivel abrir o arquivo
        {
                printf("\nErro na abertura do arquivo\n");
                exit(0);
        }

        puts("Digite um numero entre 1 e 5");//apenas uma condicao para teste


while(user_input!=0){
                scanf("%d",&user_input);
                if((user_input<0 ||user_input>5))//apenas para teste,
                        puts("Numero invalido");
                else if(user_input>0){
                        write(i2c_fd, &user_input, sizeof(user_input));   //escreve no barramento para o slave
                        sleep(1+user_input/2);//esperar o dispotivo receber e o tempo dele escrever no barramento
                        read(i2c_fd, &arduino_ret, 1);  //le pelo barramento o valor que o slave manda
                        printf("Ardunio return = %d\n",arduino_ret );
                        fprintf(fp, "Numero recebido do arduino: %d\n", arduino_ret);//escreve dentro do arquivo fp
                }}

        close(i2c_fd);//fecha o arquivo
        fclose(fp);//fecha o arquivo
        return 0;
}



