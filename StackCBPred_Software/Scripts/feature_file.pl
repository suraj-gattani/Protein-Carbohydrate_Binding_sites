open(FH,'<','id_list.txt');
while($row=<FH>){
	chomp $row;
	open(OUT,'>',"/home/avdesh/Suraj/StackCBPred_Software/Features/$row/output_$row.csv"); 
	#print OUT "B/NB,Binary(1),Binary(2),Binary(3),Binary(4),Binary(5),Binary(6),Binary(7),Binary(8),Binary(9),Binary(10),Binary(11),Binary(12),Binary(13),Binary(14),Binary(15),Binary(16),Binary(17),Binary(18),Binary(19),Binary(20),PSSM(1),PSSM(2),PSSM(3),PSSM(4),PSSM(5),PSSM(6),PSSM(7),PSSM(8),PSSM(9),PSSM(10),PSSM(11),PSSM(12),PSSM(13),PSSM(14),PSSM(15),PSSM(16),PSSM(17),PSSM(18),PSSM(19),PSSM(20),ASA,SS(1/3),SS(2/3),SS(3/3),SS(1/8),SS(2/8),SS(3/8),SS(4/8),SS(5/8),SS(6/8),SS(7/8),SS(8/8),phi,psi,HSE_up,HSE_down,disprob,CNCC(1),CNCC(2),CNCC(3),CNCC(4),CNCC(5),CNCC(6),CNCC(7),CNCC(8),PSSM_dist,PP(1),PP(2),PP(3),PP(4),PP(5),PP(6),PP(7),AA,dphi,dpsi,MG(1),BG(1),BG(2),BG(3),BG(4),BG(5),BG(6),BG(7),BG(8),BG(9),BG(10),BG(11),BG(12),BG(13),BG(14),BG(15),BG(16),BG(17),BG(18),BG(19),BG(20),sPSEE,TI(1),RF(1),RF(2),RF(3),RF(4),RF(5),RF(6),RF(7),RF(8),RF(9),RF(10),RF(11),RF(12),RF(13),RF(14),RF(15),RF(16),RF(17),RF(18),RF(19),RF(20)\n";
	print "$row\n";
	#print OUT "B/NB,PSSM(1),PSSM(2),PSSM(3),PSSM(4),PSSM(5),PSSM(6),PSSM(7),PSSM(8),PSSM(9),PSSM(10),PSSM(11),PSSM(12),PSSM(13),PSSM(14),PSSM(15),PSSM(16),PSSM(17),PSSM(18),PSSM(19),PSSM(20),ASA,phi,psi,HSE_up,HSE_down,PP(1),PP(2),PP(3),PP(4),PP(5),PP(6),PP(7),RF(1),RF(2),RF(3),RF(4),RF(5),RF(6),RF(7),RF(8),RF(9),RF(10),RF(11),RF(12),RF(13),RF(14),RF(15),RF(16),RF(17),RF(18),RF(19),RF(20)\n";

	open(FHm,'<',"/home/avdesh/Suraj/StackCBPred_Software/Features/$row/$row.i1");
		my %hashi1;
		my @lines=<FHm>;
		my $len=@lines;
		my $leng=$len;
		for($i=1;$i<=$len;$i++){
			chomp $lines[$i];
			@words=split /\s+/,$lines[$i];
			$var=$words[3].",".$words[4].",".$words[7].",".$words[8];
			$hashi1{$i-1}=$var;
			}
	open(FH7,'<',"/home/avdesh/Suraj/StackCBPred_Software/Features/$row/$row.57pfeatures");
		my %hashf;
		my @lines=<FH7>;
		my $len=@lines;
		for($i=1;$i<=$len;$i++){
			chomp $lines[$i];
			@words=split /\s+/,$lines[$i];
			#$var=$words[2].",".$words[3].",".$words[4].",".$words[5].",".$words[6].",".$words[7].",".$words[8];
			$var=$words[2].",".$words[3].",".$words[4].",".$words[5].",".$words[6].",".$words[7].",".$words[8].",".$words[9].",".$words[10].",".$words[11].",".$words[12].",".$words[13].",".$words[14].",".$words[15].",".$words[16].",".$words[17].",".$words[18].",".$words[19].",".$words[20].",".$words[21].",".$words[22].",".$words[23].",".$words[24].",".$words[25].",".$words[26].",".$words[27].",".$words[28].",".$words[32].",".$words[35];
			$hashf{$i-1}=$var;
			}
			for($keys=0;$keys<=$leng-2;$keys++){
			@aa=split /\s+/,$hashk{$keys};
			#@bb=split /\t/,$hash{$keys}
			# print $aa;
			print OUT "0,$hashi1{$keys},$hashf{$keys}\n";
			}
	}