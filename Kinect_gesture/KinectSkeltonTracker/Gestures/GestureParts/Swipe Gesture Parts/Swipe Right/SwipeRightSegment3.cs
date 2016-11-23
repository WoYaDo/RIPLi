// -----------------------------------------------------------------------
// <copyright file="SwipeRightSegment3.cs" company="Microsoft Limited">
//  Copyright (c) Microsoft Limited, Microsoft Consulting Services, UK. All rights reserved.
// All rights reserved.
// THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
// </copyright>
// <summary>Description</summary>
//-----------------------------------------------------------------------
namespace KinectSkeltonTracker.Gestures.GestureParts
{
    #region using...

    using Microsoft.Research.Kinect.Nui;

    #endregion

    /// <summary>
    /// The third part of the swipe right gesture
    /// </summary>
    public class SwipeRightSegment3 : IRelativeGestureSegment
    {
        /// <summary>
        /// Checks the gesture.
        /// </summary>
        /// <param name="skeleton">The skeleton.</param>
        /// <returns>GesturePartResult based on if the gesture part has been completed</returns>
        public GesturePartResult CheckGesture(Microsoft.Research.Kinect.Nui.SkeletonData skeleton)
        {
            // //left hand in front of left Shoulder
            if (skeleton.Joints[JointID.HandLeft].Position.Z < skeleton.Joints[JointID.ElbowLeft].Position.Z && skeleton.Joints[JointID.HandRight].Position.Y < skeleton.Joints[JointID.HipCenter].Position.Y)
            {
                // Debug.WriteLine("GesturePart 2 - left hand in front of left Shoulder - PASS");
                // //left hand below shoulder height but above hip height
                if (skeleton.Joints[JointID.HandLeft].Position.Y < skeleton.Joints[JointID.Head].Position.Y && skeleton.Joints[JointID.HandLeft].Position.Y > skeleton.Joints[JointID.HipCenter].Position.Y)
                {
                    // Debug.WriteLine("GesturePart 2 - left hand below shoulder height but above hip height - PASS");
                    // //left hand left of left Shoulder
                    if (skeleton.Joints[JointID.HandLeft].Position.X > skeleton.Joints[JointID.ShoulderRight].Position.X)
                    {
                        // Debug.WriteLine("GesturePart 2 - left hand left of left Shoulder - PASS");
                        return GesturePartResult.Suceed;
                    }

                    // Debug.WriteLine("GesturePart 2 - left hand left of left Shoulder - UNDETERMINED");
                    return GesturePartResult.Pausing;
                }

                // Debug.WriteLine("GesturePart 2 - left hand below shoulder height but above hip height - FAIL");
                return GesturePartResult.Fail;
            }

            // Debug.WriteLine("GesturePart 2 - left hand in front of left Shoulder - FAIL");
            return GesturePartResult.Fail;
        }
    }
}
