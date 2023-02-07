class Solution {
    
    
    public int carFleet(int target, int[] position, int[] speed) {
        
        CarState[] carStates = new CarState[position.length];
        
        for (int i = 0; i < position.length; i++) {
            carStates[i] = new CarState(target - position[i], speed[i], 1.0*(target - position[i])/speed[i]);
        }
        
        Arrays.sort(carStates, new Comparator<CarState>() {
            public int compare(CarState state1, CarState state2) {
                return state1.distanceFromTarget - state2.distanceFromTarget;
            }
        });
        
        int fleetCount = 0;
        double prevTime = 0.0;
        
        for (int i = 0; i < carStates.length; i++) {
            if (carStates[i].time > prevTime) {
                fleetCount++;
                prevTime = carStates[i].time;
            }
        }
        
        return fleetCount;
    }
}

class CarState {
    
    public int distanceFromTarget;
    
    public int speed;
    
    public double time;
    
    public CarState(int distanceFromTarget, int speed, double time) {
        this.distanceFromTarget = distanceFromTarget;
        this.speed = speed;
        this.time = time;
    }
}