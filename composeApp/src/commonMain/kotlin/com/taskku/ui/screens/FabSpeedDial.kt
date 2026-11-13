package com.taskku.ui.screens

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.core.tween
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.Notifications
import androidx.compose.material.icons.rounded.Close
import androidx.compose.material.icons.rounded.Edit
import androidx.compose.material.icons.rounded.Tag
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.taskku.theme.LocalTaskKuColors
import com.taskku.theme.LocalTaskKuText
import com.taskku.ui.FabButton

private data class DialAction(val label: String, val icon: ImageVector, val primary: Boolean)

private val dialActions = listOf(
    DialAction("Pengingat", Icons.Rounded.Notifications, false),
    DialAction("Kategori Baru", Icons.Rounded.Tag, false),
    DialAction("Tugas Baru", Icons.Rounded.Edit, true),
)

@Composable
fun FabSpeedDial(
    expanded: Boolean,
    onDismiss: () -> Unit,
    onAction: (String) -> Unit,
) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    val rotation by animateFloatAsState(
        targetValue = if (expanded) 45f else 0f,
        animationSpec = tween(200),
        label = "fabRotate",
    )

    AnimatedVisibility(
        visible = expanded,
        enter = fadeIn(tween(150)),
        exit = fadeOut(tween(150)),
    ) {
        Box(
            Modifier
                .fillMaxSize()
                .background(Color(0xFF13131966))
                .clickable(onClick = onDismiss),
        ) {
            Column(
                verticalArrangement = Arrangement.spacedBy(14.dp),
                horizontalAlignment = Alignment.End,
                modifier = Modifier
                    .align(Alignment.BottomEnd)
                    .padding(end = 24.dp, bottom = 168.dp),
            ) {
                dialActions.forEach { action ->
                    AnimatedVisibility(visible = expanded, enter = fadeIn(tween(150)), exit = fadeOut(tween(100))) {
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.spacedBy(10.dp),
                        ) {
                            Box(
                                contentAlignment = Alignment.Center,
                                modifier = Modifier
                                    .clip(RoundedCornerShape(999.dp))
                                    .background(colors.surface)
                                    .clickable { onAction(action.label) }
                                    .padding(horizontal = 14.dp, vertical = 9.dp),
                            ) {
                                Text(
                                    action.label,
                                    style = txt.small.copy(
                                        fontWeight = androidx.compose.ui.text.font.FontWeight.SemiBold,
                                        fontSize = 12.5.sp,
                                    ),
                                    color = if (action.primary) colors.primary else colors.text,
                                )
                            }
                            Box(
                                contentAlignment = Alignment.Center,
                                modifier = Modifier
                                    .size(48.dp)
                                    .clip(CircleShape)
                                    .background(if (action.primary) colors.primary else colors.surface)
                                    .clickable { onAction(action.label) },
                            ) {
                                Icon(
                                    action.icon,
                                    contentDescription = action.label,
                                    tint = if (action.primary) colors.primaryFg else colors.text,
                                    modifier = Modifier.size(20.dp),
                                )
                            }
                        }
                    }
                }
            }
            FabButton(
                onClick = onDismiss,
                modifier = Modifier
                    .align(Alignment.BottomEnd)
                    .padding(end = 24.dp, bottom = 90.dp),
                icon = Icons.Rounded.Close,
                rotation = rotation,
            )
        }
    }
}
