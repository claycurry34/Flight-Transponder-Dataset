import sys


if __name__ == "__main__":
    # start()
    from adsbexchange.connection.connectionmanager import ConnectionManager
    from adsbexchange.persistence.airspace import Airspace
    from adsbexchange.persistence.aircraft import Aircraft
    
    conn: ConnectionManager = None
    try:
        from adsbexchange.connection.connectionmanager import ConnectionManager
        from adsbexchange.persistence.airspace import Airspace
        united_states = [3, 2, 44, 5979, 6100, 6221, 6342, 6463, 6584, 4, 5980, 6101, 6222, 6343, 6464, 6585, 5981, 6102, 6223, 6344, 5, 45, 5861, 5982, 6103, 6224, 6345, 5862, 5983, 6104, 6225, 6346, 6, 5863, 5984, 6105, 6226, 6347, 5864, 5985, 6106, 6227, 6348, 5865, 5986, 6107, 6228, 6349, 46, 5745, 5866, 5987, 6108, 6229, 6350, 7, 5746, 5867, 5988, 6109, 6230, 6351, 5747, 5868, 5989, 6110, 6231, 6352, 5748, 5869, 5990, 6111, 6232, 6353, 49, 47, 5870, 5991, 6112, 6233, 6354, 8, 5871, 5992, 6113, 6234, 6355, 5630, 5751, 5872, 5993, 6114, 6235, 6356, 5631, 5752, 5873, 5994, 6115, 6236, 6357, 5632, 5753, 5874, 5995, 6116, 6237, 6358, 55, 6238, 6359, 9, 6239, 6360, 56, 57]
        air_sp = Airspace(united_states)
        ac = Aircraft('A7D32E')
        conn = ConnectionManager()
        conn.add_airspace(air_sp)
        #conn.add_aircraft(ac)
        while True:
            pass
    except Exception as e:
        print(e)