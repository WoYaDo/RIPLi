   M S B A M L   `   `   `  ���� O  KKinectSkeltonTracker, Version=1.0.0.0, Culture=neutral, PublicKeyToken=nullQ-clr-namespace:KinectSkeltonTracker.ConvertersKinectSkeltonTracker.Converters  %    KinectSkeltonTracker.MainWindow   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     ?local-clr-namespace:KinectSkeltonTracker.Converters       � Title$  
MainWindow��$	��350��$	��525�� � 	Resources @   :KinectSkeltonTracker.Converters.JointToVisibilityConverter   JointToVisibilityConverterN   HKinectSkeltonTracker.Converters.KinectValueToScreenCoOrdinatesConverterY , (KinectValueToScreenCoOrdinatesConverterYN   HKinectSkeltonTracker.Converters.KinectValueToScreenCoOrdinatesConverterX , (KinectValueToScreenCoOrdinatesConverterXE   ?KinectSkeltonTracker.Converters.ColorToSolidColorBrushConverter # ColorToSolidColorBrushConverter?   9KinectSkeltonTracker.Converters.BoolToVisibilityConverter  BoolToVisibilityConverter��%K   &	        &	      &	 
     &	      &	                .��� .+��� 
�������.+��� -   $��SkeletonControl������ .R�� ���� .R��� .+��� $��50,100,50,100q�$��30(�
���  ������ *GestureText+y��� *GestureDetected+ �� 	Converter# [ �� $��3��
���   � �� StrokeEndLineCap$ Round=�
���   �	 �� X1 �� *LeftHand.Position.X+# [  �� ConverterParameter$ 7��	 �� Y1 �� *LeftHand.Position.Y+# [ $ 7��	 �� X2 �� *LeftWrist.Position.X+# [ $ 7��	 �� Y2 �� *LeftWrist.Position.Y+# [ $ 7���� $��3��
���   �$ Round=�
���   � �� *LeftHand.Position.X+# [ $ 7�� �� *LeftHand.Position.Y+# [ $ 7�� �� *LeftWrist.Position.X+# [ $ 7�� �� *LeftWrist.Position.Y+# [ $ 7���� $��3��
���   �$ Round=�
���   � �� *LeftWrist.Position.X+# [ $ 7�� �� *LeftWrist.Position.Y+# [ $ 7�� �� *LeftElbow.Position.X+# [ $ 7�� �� *LeftElbow.Position.Y+# [ $ 7���� $��3��
���   �$ Round=�
���   � �� *LeftElbow.Position.X+# [ $ 7�� �� *LeftElbow.Position.Y+# [ $ 7�� �� *ShoulderCenter.Position.X+# [ $ 7�� �� *ShoulderCenter.Position.Y+# [ $ 7���� $��3��
���   �$ Round=�
���   � �� *ShoulderCenter.Position.X+# [ $ 7�� �� *ShoulderCenter.Position.Y+# [ $ 7�� �� *Head.Position.X+# [ $ 7�� �� *Head.Position.Y+# [ $ 7���� $��3��
���   �$ Round=�
���   � �� *ShoulderCenter.Position.X+# [ $ 7�� �� *ShoulderCenter.Position.Y+# [ $ 7�� �� *RightElbow.Position.X+# [ $ 7�� �� *RightElbow.Position.Y+# [ $ 7���� $��3��
���   �$ Round=�
���   � �� *RightElbow.Position.X+# [ $ 7�� �� *RightElbow.Position.Y+# [ $ 7�� �� *RightWrist.Position.X+# [ $ 7�� �� *RightWrist.Position.Y+# [ $ 7���� $��3��
���   �$ Round=�
���   � �� *RightWrist.Position.X+# [ $ 7�� �� *RightWrist.Position.Y+# [ $ 7�� �� *RightHand.Position.X+# [ $ 7�� �� *RightHand.Position.Y+# [ $ 7���� $��3��
���   �$ Round=�
���   � �� *ShoulderCenter.Position.X+# [ $ 7�� �� *ShoulderCenter.Position.Y+# [ $ 7�� �� *Spine.Position.X+# [ $ 7�� �� *Spine.Position.Y+# [ $ 7���� $��3��
���   �$ Round=�
���   � �� *Spine.Position.X+# [ $ 7�� �� *Spine.Position.Y+# [ $ 7�� �� *HipCenter.Position.X+# [ $ 7�� �� *HipCenter.Position.Y+# [ $ 7���� $��3��
���   �$ Round=�
���   � �� *HipCenter.Position.X+# [ $ 7�� �� *HipCenter.Position.Y+# [ $ 7�� �� *LeftKnee.Position.X+# [ $ 7�� �� *LeftKnee.Position.Y+# [ $ 7���� $��3��
���   �$ Round=�
���   � �� *HipCenter.Position.X+# [ $ 7�� �� *HipCenter.Position.Y+# [ $ 7�� �� *RightKnee.Position.X+# [ $ 7�� �� *RightKnee.Position.Y+# [ $ 7���� $��3��
���   �$ Round=�
���   � �� *RightKnee.Position.X+# [ $ 7�� �� *RightKnee.Position.Y+# [ $ 7�� �� *RightAnkle.Position.X+# [ $ 7�� �� *RightAnkle.Position.Y+# [ $ 7���� $��3��
���   �$ Round=�
���   � �� *LeftKnee.Position.X+# [ $ 7�� �� *LeftKnee.Position.Y+# [ $ 7�� �� *LeftAnkle.Position.X+# [ $ 7�� �� *LeftAnkle.Position.Y+# [ $ 7���� $��3��
���   �$ Round=�
���   � �� *RightAnkle.Position.X+# [ $ 7�� �� *RightAnkle.Position.Y+# [ $ 7�� �� *RightFoot.Position.X+# [ $ 7�� �� *RightFoot.Position.Y+# [ $ 7���� $��3��
���   �$ Round=�
���   � �� *LeftAnkle.Position.X+# [ $ 7�� �� *LeftAnkle.Position.Y+# [ $ 7�� �� *LeftFoot.Position.X+# [ $ 7�� �� *LeftFoot.Position.Y+# [ $ 7��A� $��LeftHand��$��14��
���   �$��14������ *
JointColor+# [ y��� *
LeftHand+# [  z�T� 	 T� X	 �� *LeftHand.Position.X+# [ $ 0��
 T� Y
 �� *LeftHand.Position.Y+# [ $ 0��A� $��	RightHand��$��14��
���   �$��14������ *
JointColor+# [ y��� *	RightHand+# [  z�T� 	 �� *RightHand.Position.X+# [ $ 0��
 �� *RightHand.Position.Y+# [ $ 0��A� $��	LeftWrist��$��14��
���   �$��14������ *
JointColor+# [ y��� *	LeftWrist+# [  z�T� 	 �� *LeftWrist.Position.X+# [ $ 0��
 �� *LeftWrist.Position.Y+# [ $ 0��A� $��
RightWrist��$��14��
���   �$��14������ *
JointColor+# [ y��� *
RightWrist+# [  z�T� 	 �� *RightWrist.Position.X+# [ $ 0��
 �� *RightWrist.Position.Y+# [ $ 0��A� $
��Head��$��70��
���   �$��70������ *
JointColor+# [ y��� *Head+# [  z�T� 	 �� *Head.Position.X+# [ $	 -28��
 �� *Head.Position.Y+# [ $	 -28��A� $��ShoulderCenter��$��14��
���   �$��14������ *
JointColor+# [ y��� *ShoulderCenter+# [  z�T� 	 �� *ShoulderCenter.Position.X+# [ $ 0��
 �� *ShoulderCenter.Position.Y+# [ $ 0��A� $��Spine��$��14��
���   �$��14������ *
JointColor+# [ y��� *Spine+# [  z�T� 	 �� *Spine.Position.X+# [ $ 0��
 �� *Spine.Position.Y+# [ $ 0��A� $��	HipCenter��$��14��
���   �$��14������ *
JointColor+# [ y��� *	HipCenter+# [  z�T� 	 �� *HipCenter.Position.X+# [ $ 0��
 �� *HipCenter.Position.Y+# [ $ 0��A� $��LeftKnee��$��14��
���   �$��14������ *
JointColor+# [ y��� *
LeftKnee+# [  z�T� 	 �� *LeftKnee.Position.X+# [ $ 0��
 �� *LeftKnee.Position.Y+# [ $ 0��A� $��	RightKnee��$��14��
���   �$��14������ *
JointColor+# [ y��� *	RightKnee+# [  z�T� 	 �� *RightKnee.Position.X+# [ $ 0��
 �� *RightKnee.Position.Y+# [ $ 0��A� $��	LeftAnkle��$��14��
���   �$��14������ *
JointColor+# [ y��� *	LeftAnkle+# [  z�T� 	 �� *LeftAnkle.Position.X+# [ $ 0��
 �� *LeftAnkle.Position.Y+# [ $ 0��A� $��
RightAnkle��$��14��
���   �$��14������ *
JointColor+# [ y��� *
RightAnkle+# [  z�T� 	 �� *RightAnkle.Position.X+# [ $ 0��
 �� *RightAnkle.Position.Y+# [ $ 0��A� $��LeftFoot��$��14��
���   �$��14������ *
JointColor+# [ y��� *
LeftFoot+# [  z�T� 	 �� *LeftFoot.Position.X+# [ $ 0��
 �� *LeftFoot.Position.Y+# [ $ 0��A� $��	RightFoot��$��14��
���   �$��14������ *
JointColor+# [ y��� *	RightFoot+# [  z�T� 	 �� *RightFoot.Position.X+# [ $ 0��
 �� *RightFoot.Position.Y+# [ $ 0��A� $��	LeftElbow��$��14��
���   �$��14������ *
JointColor+# [ y��� *	LeftElbow+# [  z�T� 	 �� *LeftElbow.Position.X+# [ $ 0��
 �� *LeftElbow.Position.Y+# [ $ 0��A� $��
RightElbow��$��14��
���   �$��14������ *
JointColor+# [ y��� *
RightElbow+# [  z�T� 	 �� *RightElbow.Position.X+# [ $ 0��
 �� *RightElbow.Position.Y+# [ $ 0���� 
���   �$��2q�$	��260��$	��200��$��0,5,5,0q�$	��Top=�$��Right=�._��� -   $��
cameraFeed��$	��200��$
��Fill=�$	��260������ *CameraImage+