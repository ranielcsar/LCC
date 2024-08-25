class TV:
    def __init__(self, canal: int, volume: int):
        self._max_canais = 10
        self._max_volume = 60
        self.__volume = volume
        self.__canal = canal

    def canal_anterior(self) -> None:
        if self.__canal > 0:
            self.__canal -= 1
            return
                
        self.__canal = self._max_canais
    
    def proximo_canal(self) -> None:
        if self.__canal < self._max_canais:
            self.__canal += 1
            return
                
        self.__canal = 0

    def aumentar_volume(self) -> None:
        if self.__volume < self._max_volume:
            self.__volume += 5        

    def diminuir_volume(self) -> None:
        if self.__volume > 0:
            self.__volume -= 5 
        
    def __str__(self) -> str:
        text = "--------------------------------------------------\n"
        text += f"[Informações sobre a TV]\nCanal atual: {self.__canal}\nVolume atual: {self.__volume}\n"
        text += "--------------------------------------------------"
        return text

        