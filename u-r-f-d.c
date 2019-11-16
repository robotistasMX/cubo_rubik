int n;
int dg2=91;
int mt[]={0,motorA,motorB,motorC,motorD,0,0,motorA,motorB,motorC,motorD,0,0};
int dir[]={0,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1};
int dg[]={0,90.5,90,91,91.5,91,91,90.5,90,91,91.5,91,91};
//					U  R  F  D  L  B  U  R  F  D  L  B
task main(){
	int moves[]={0,7,3,3,10,5,5,12,7,5,10,8,3,2,3,3,10,6,6,1,2,2,1,2,2,5,5,4};
	int robot[]={0,1,1,1,1,0,0,0,1,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1};
	n=27;



	clearTimer(T1);
	for(int j=1; j<=n; j++){
		if(robot[j]==1){
			setMotorTarget(mt[moves[j]],	getMotorEncoder(mt[moves[j]])+(dg[moves[j]]*dir[moves[j]]), 60);
			waitUntilMotorStop(mt[moves[j]]);
		}
		waitUntil(time1[T1]>(j*600));
	}
}
