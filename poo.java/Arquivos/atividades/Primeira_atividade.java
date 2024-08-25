package ranoob_atividades;

public class Primeira_atividade {
    public static void main(String []args)
    {       
        String frase = "casa suja ch�o sujo";
        
        System.out.println("Frase usada: " + frase + "\n");
        
        // A
        int tamanho = frase.length();
        
        System.out.println("Total de caracteres da frase: " + tamanho + "\n");
        
        // B
        System.out.println("Frase escrita em maiusculo: " + frase.toUpperCase() + "\n");
        
        // C
        int contaVogais = 0;
        
        frase.toLowerCase();
        
        for (int i = 0; i < tamanho; i++)
        {
            char caractere = frase.charAt(i);
            
            if (caractere == 'a' ||  caractere == 'e' ||  caractere == 'i' ||  caractere == 'o' ||  caractere == 'u')
            {
                contaVogais++;
            }
        }
        
        System.out.println("Total de vogais na frase: " + contaVogais + "\n");
        
        // D
        String nome = "unirio";
        
        System.out.println("Nome usado: " + nome + "\n");
        
        if (nome.startsWith("uni"))
        {
            System.out.println("O nome come�a com UNI. \n");
        } else {
            System.out.println("O nome n�o come�a com UNI. \n");
        }
        
        // E
        if (nome.endsWith("rio"))
        {
            System.out.println("A nome termina com RIO. \n");
        } else {
            System.out.println("A nome n�o termina com RIO. \n");
        }
        
        // F
        frase = "N01S � V1D4 L0K4";
        tamanho = frase.length();
        int contaNumeros = 0;
        
        System.out.println("Frase usada: " + frase + "\n");
        
        for (int i = 0; i < tamanho; i++)
        {
            if (Character.isDigit(frase.charAt(i)))
            {
                contaNumeros++;
            }
        }
        
        System.out.println("Sua frase tem " + contaNumeros + " n�meros. \n");
        
        
        // G
        nome = "arara";
        
        System.out.println("Nome usado: " + nome + "\n");
        
        String nomeInvertido = new StringBuffer(nome).reverse().toString();
        
        if (nome.equalsIgnoreCase(nomeInvertido))
        {
            System.out.println("Seu nome � um palindromo. \n");
        } else {
            System.out.println("Seu nome n�o � um palindromo. \n");
        }
    }
}
