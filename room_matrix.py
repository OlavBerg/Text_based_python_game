from room import Room

class RoomMatrix:
    def __init__(self, roomList: list[Room]):
        numOfRows = max(room.getCoordinates()[0] for room in roomList) + 1
        numOfColumns = max(room.getCoordinates()[1] for room in roomList) + 1

        self.matrix = self.emptyMatrix(numOfRows, numOfColumns)

        for room in roomList:
            coordinates = room.getCoordinates()
            xCoordinate = coordinates[0]
            yCoordinate = coordinates[1]

            self.matrix[xCoordinate][yCoordinate] = room
            
    def emptyMatrix(self, numOfRows: int, numOfColumns: int):
        matrix = []

        for i in range(numOfRows):
            row = []

            for i in range(numOfColumns):
                row.append(None)
            
            matrix.append(row)
        
        return matrix

    def getRoom(self, xCoordinate: int, yCoordinate: int):
        #print(self.matrix[xCoordinate][yCoordinate])
        return self.matrix[xCoordinate][yCoordinate]


