#include <stdio.h>
#include <string.h>
#include <locale.h>
#include <stdlib.h>
#include <ctype.h>
#include "funcoes.h"

int main()
{
	setlocale(LC_ALL,"");
	char palavra[20],pFinal[20],letra,letraUsada[20];
	char nome[20];
	int vit=0,der=0;
	int numErros,verificaErro,numLetras,contaAcertos,contaLetras,win,verificaLetra=1,letraRep;
	int sair=1,opcaoTemas,opcaoMenu;
	int i; //Contadora
	FILE *arq,*rank;
	rank=fopen("arquivos/rank.txt","a+");
	
	if (rank==NULL)
	{
		printf("Arquivo n�o encontrado!\n");
	}	
		
	load();
	
	do
	{
		menuPrincipal();
		scanf("%d",&opcaoMenu);
		printf("\n");
		if (opcaoMenu==1)
		{
			mostraRank();
		}
		system("cls");
	} while (opcaoMenu!=2);
	
	intro();		
	
	printf("Digite seu nome: ");	
	scanf("%s",nome);
	fprintf(rank,"%s ",nome); //Guarda nome no rank.txt
	printf("\n\n");				
	
	do
	{
		//Inicia as vari�veis e, caso o jogador queira jogar novamente, zera todas
		numErros=0;
		numLetras=0;
		contaAcertos=0;
		contaLetras=0;
		win=0;		
		
		do
		{
			menuTemas();	
			scanf("%d",&opcaoTemas);
					
			if (opcaoTemas>2)
			{
				printf("Op��o inv�lida! Tente novamente >\n\n");			
			}		
		} while (opcaoTemas>2);
		
	
		if (opcaoTemas==1)
		{
			arq=fopen("arquivos/animais.txt","r");
			strcpy(palavra,buscaPalavra(arq));
		}
	
		if (opcaoTemas==2)
		{
			arq=fopen("arquivos/frutas.txt","r");
			strcpy(palavra,buscaPalavra(arq));
		}
		system("cls");
		fflush(stdin); //Limpa mem�ria tempor�ria
		
		/* O fflush(stdin) foi usado pois, quando a vari�vel "palavra" recebe a "palavraRandom" da fun��o buscaPalavra,
			vem com um "\n" no final, o que acaba ocasionando um bug em que a vari�vel "letra" recebe \n e, quando
			o loop verifica as letras, conta como erro. Por isso foi necess�rio limpar o buffer.*/
		
		numLetras=strlen(palavra)-1; /*Conta o total de letras na palavra (o -1 � pra n�o contar o \n).
		 							   Mesmo depois da "limpeza" no buffer, o \n ainda � contado*/
		
		//Adiciona espa�o em branco nos vetores para evitar caracteres estranhos durante a execu��o
		for (i=0; i<numLetras; i++)
		{
			pFinal[i]=' ';
			letraUsada[i]=' ';						
		}
		
		printf("\n\n");
		printf("Palavra: ");			
		for (i=0; i<numLetras; i++)
		{
			if (pFinal[i]==' ')
			{
				printf("_ ");
			}
		}
		
		printf("%*s",25-numLetras," "); //Usado para manipular a tabula��o do printf abaixo 25 espa�os - num�ro de letras da pakavra
		printf("Letras usadas: ");
		for (i=0; i<contaLetras; i++)
		{
			printf("%c ",toupper(letraUsada[i]));						
		}			
		printf("\n\n");	
	
		while (win==0)
		{
			printf("\n");		
			printf("Erros: %d\t\t N�mero de letras da palavra: %d\n\n",numErros,numLetras);
			boneco(numErros);
			printf("Letra: ");						
			
			//Loop usado para ler outra letra, caso a mesma seja igual a alguma j� usada			
			do
			{	
				scanf("%c",&letra);
				fflush(stdin);				
				
				verificaLetra=0;
				letraRep=0;																	
				
				//Verifica se a letra j� foi usada
				if (contaLetras>0)
				{
					for (i=0; i<contaLetras; i++)
					{
						if (letra==letraUsada[i])
						{
							printf("Esta letra j� foi usada! Tente novamente.");
							verificaLetra=1;
							numErros++;
							sleep(2);
							
							if (numErros==6)
							{
								win=1;
							}								
						} 												  
					}
					
					if (letra!=letraUsada[i])
					{
						verificaLetra=0;
					}
				}
									
			} while (verificaLetra!=0);			
			
			//Guarda as letras usadas no vetor e, se for a mesma letra, n�o guarda
			if (letra!=letraUsada[i])
			{
				for (i=0; i<contaLetras; i++)
				{
					if (letra==letraUsada[i])
					{
						letraRep=1;
					}
				}
				
				if (letraRep!=1)
				{
					for (i=contaLetras; i<contaLetras+1; i++) 
					{
						letraUsada[i]=letra;
					}
				}				
			}			
			letraRep=0;
			
			contaLetras++; //Vari�vel que conta quantas letras foram digitadas				
	
			fflush(stdin);
			verificaErro=0;
	
			for (i=0; i<numLetras; i++)
			{
				if (letra==palavra[i])
				{
					if (letra!=pFinal[i])
					{
						contaAcertos++;
					}
					
					pFinal[i]=letra;
					verificaErro=1;															
				}															
			}			
	
			if (verificaErro==0)
			{
				numErros++;
				if (numErros==6)
				{
					win=1;
				}
			}
	
			if (contaAcertos==numLetras)
			{
				win=2;
			}
			system("cls");
			printf("\n\n");
			
			printf("Palavra: "); //Palavra que ser� encontrada			
			for (i=0; i<numLetras; i++)
			{
				if (pFinal[i]==' ')
				{
					printf("_ ");
				} else 
				{
					printf("%c ",toupper(pFinal[i]));
				}			
			}
			
			printf("%*s",25-numLetras," ");
			printf("Letras usadas: "); //Mostra as letras que o usu�rio digitou
			for (i=0; i<contaLetras; i++)
			{
				if (letraUsada[i]==' ')
				{
					printf("- ");
				} else
				{
					printf("%c ",toupper(letraUsada[i]));
				}														
			}					
			printf("\n\n");				
		} 
		printf("\n");		
		
		
		
		if (win==1)
		{
			der++;			
		} else	
		{
			vit++;			
		}	
	
		if (win==1)
		{
			boneco(6);
			printf("Voc� perdeu, %s :'(\n\n",nome);
			printf("A palavra era: %s\n",palavra);			
		}
		
		if (win==2)
		{
			boneco(7);
			printf("Parab�ns, %s! Voc� ganhou! \\o/\n\n",nome);
			printf("Total de erros: %d\n\n",numErros);					
		}
		
		printf("Deseja jogar novamente?\n");
		printf("1. Sim\n");
		printf("2. N�o\n");
		scanf("%d",&sair);
		printf("\n");	
		
	} while (sair==1);
	fprintf(rank,"%d %d\n",vit,der);	
	
	printf("\n");
	printf("OBRIGADO POR JOGAR! VOLTE SEMPRE!\n\n");
	cred();		
}
